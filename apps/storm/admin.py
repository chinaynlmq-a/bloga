from django.contrib import admin
from .models import Article, Tag, Category, Carousel, Keyword, FriendLink, BigCategory,Activate


#装饰器 使用装饰函数在admin管理后台中注册
@admin.register(Article)
# 定制后台管理页面
class ArticleAdmin(admin.ModelAdmin):
    '''
     ModelAdmin.date_hierarchy
     根据你指定的日期相关的字段，为页面创建一个时间导航栏，可通过日期过滤对象
    '''
    # 这个的作用是给出一个筛选机制，一般按照时间比较好
    date_hierarchy = 'create_date'

    '''
    ModelAdmin.exclude
    不显示指定的某些字段
    # 一定注意了，值是个元组！一个元素的时候，最后的逗号不能省略。
    '''
    exclude = ('views',)

    '''
    ModelAdmin.list_display
    指定显示在修改页面上的字段。这是一个很常用也是最重要的技巧之一。
    如果你不设置这个属性，admin站点将只显示一列，内容是每个对象的__str__()(Python2使用__unicode__())方法返回的内容。
    '''

    # 在查看修改的时候显示的属性，第一个字段带有<a>标签，所以最好放标题
    list_display = ('id', 'title', 'author', 'create_date', 'update_date')

    '''
    ModelAdmin.list_display_links
    指定用于链接修改页面的字段。通常情况，list_display列表中的第一个元素被作为指向目标修改页面的超级链接点。
    但是，使用list_display_links可以帮你修改这一默认配置。
    '''
    # 设置需要添加<a>标签的字段
    list_display_links = ('title',)
    
    '''
    ModelAdmin.list_filter
    设置list_filter属性后，可以激活修改列表页面的右侧边栏，用于对列表元素进行过滤
    '''
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

@admin.register(Activate)
class ActivateAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_active')
