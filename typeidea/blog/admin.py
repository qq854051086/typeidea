from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


# Register your models here.
from .models import Post, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner','status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav', 'created_time', 'owner')
    #这里重写的save_model方法，即使用户选择其他用户，也会被写入为当前用户

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status', 'created_time')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status',
                    'created_time', 'operator'
    ]
    list_display_links = []  #点击那些字段可以进入编辑

    list_filter = ['category',]
    search_fields = ['title', 'category__name']


    # actions_on_top = True   #可选列表的批量删除动作相关，是否展示在顶部
    # actions_on_bottom = True  #动作相关，是否展示在顶部

    #编辑页面
    save_on_top = True    #保存、编辑、编辑并新建按钮是否在顶部展示

    fields = (
        ('category', 'title'),
        'desc', 'status', 'content',
        'tag',
    )   #元组用于在同一行展示字段

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'    #自定义字段

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
