from django.contrib import admin
from .models import Article, Tag, Category, Carousel, Keyword, FriendLink, BigCategory

#装饰器 使用装饰函数在admin管理后台中注册
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    date_hierarchy = 'create_date'

    exclude = ('views',)

    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'create_date', 'update_date')

    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)

    # 激活过滤器，这个很有用
    list_filter = ('create_date', 'category')

    list_per_page = 50  # 控制每页显示的对象数量，默认是100

    filter_horizontal = ('tags', 'keywords')  # 给多选增加一个左右添加的框

    # 限制用户权限，只能看到自己编辑的文章
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')


@admin.register(BigCategory)
class BigCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'slug')


# 自定义管理站点的名称和URL标题
admin.site.site_header = '网站管理'
admin.site.site_title = '博客后台管理'


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'content', 'img_url', 'url')


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(FriendLink)
class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link', 'create_date', 'is_active', 'is_show')
    date_hierarchy = 'create_date'
    list_filter = ('is_active', 'is_show')
