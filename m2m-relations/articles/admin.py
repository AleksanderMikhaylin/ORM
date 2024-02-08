from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = 0
        for form in self.forms:
            is_main += form.cleaned_data.get('is_main', 0)
            if is_main == 2:
                raise ValidationError('Основной раздел должен быть один!')

        if is_main == 0:
            raise ValidationError('Не задан основной раздел!')

        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['is_main']
    inlines = [ScopeInline, ]
