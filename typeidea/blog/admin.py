from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from .adminforms import PostAdminForm
from .models import Post, Category, Tag
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site

# Register your models here.

class PostInline(admin.TabularInline):   #可选择继承admin。StackedInline，以获取不同的展示样式
    fields = ('title','desc')
    extra = 1  #控制额外多几个
    model = Post


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline,]
    list_display = ('name', 'owner','status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav', 'created_time')

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


class CategoryOwnerFilter(admin.SimpleListFilter):
    '''自定义过滤器之展示当前用户分类'''
    title = '分类过滤器'
    parameter_name= 'owner_category'
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status', 'created_time')


# @admin.register(Post)   #默认站点配置
@admin.register(Post, site=custom_site)    #自定义站点（url）

class PostAdmin(BaseOwnerAdmin):
    list_display = ['title', 'category', 'status',
                    'created_time', 'owner', 'operator'
    ]
    list_display_links = []  #点击那些字段可以进入编辑

    list_filter = [CategoryOwnerFilter, ]   #自定义右侧过滤内容为当前用户的内容
    search_fields = ['title', 'category__name']   #__指定搜索关联model的数据，这种方法可用于list_display\list_filter


    # actions_on_top = True   #可选列表的批量删除动作相关，是否展示在顶部
    # actions_on_bottom = True  #动作相关，是否展示在顶部

    #编辑页面
    save_on_top = True    #保存、编辑、编辑并新建按钮是否在顶部展示

    exclude = ('owner',)    #指定哪些字段不展示.

    '''
    fields = (
        ('category', 'title'),
        'desc', 'status', 'content',
        'tag'
    )   #元组用于在同一行展示字段
    '''

    fieldsets = (
        ('基础配置',{
            'description': '基础配置描述',
            'fields':(
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容',{
            'fields':(
                'desc','content',
            ),
        }),
        ('额外信息',{
            'classes':('collapse',),
            'fields':('tag',),
        })
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'    #自定义字段

    # form = PostAdminForm    #自定义的form格式


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']