## 此处记录有关笔记

1. sublime没有Package Settings 和Package Control的问题

   ```
   参考链接：
   	https://www.cnblogs.com/fx2008/p/5286773.html
   ```

   使用Ctrl+`快捷键或者通过View->Show Console菜单打开命令行，粘贴如下代码：

   ```
   import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
   ```

   如果顺利的话，此时就可以在Preferences菜单下看到Package Settings和Package Control两个菜单了。

   然后install package   --->  chinese
   
2. setup.py文件的作用

   ```
   	该文件于requeirment.txt有类似作用。正式环境中用到的东西会放到setup.py的indstall_requires中，而开发环境的依赖项放到requirement.txt中
   	requirement中开头的-i指定镜像地址，-e表示从当前的setup.py中查找其他依赖项
   
   ```

   示例requeirment.txt内容如下

   ```txt
   -i http://pypi.doubanio.com/simple/
   Django~=1.11
   -e
   ```

3. setting的拆分测试

4. 语录：“复杂的东西抽象成基类，有特性的东西抽出来作为子类”

5. ForeignKey 的基本属性

   ```
   至少需要指定3个参数，
   owner = models.ForeignKey(User, verbose_name='作者',on_delete=models.DO_NOTHING)
   #拓展
   #关联表数据删除时，被关联表数据的行为(以作者与书的关系进行解释)
   in_delete=models.DO_NOTHING   字面的意思，啥也不干，你删除你的干我毛线关系
   				CASCADE：都删除；
   				PROTECT：删除作者的信息时，采取保护机制，抛出错误：即不删除Books的内容；
   				SET_NULL：只有当null=True才将关联的内容置空；
   				SET_DEFAULT：设置为默认值；
   				SET( )：括号里可以是函数，设置为自己定义的东西；
   
   ```

6. INSTALLED_APPS中的顺序所代表的含义

   ```
   静态资源按照这个顺序去查找，如果要重写django自带的admin模板，可采用路径和名称一模一样的方式，自动加载你的(如果你的APP靠前),但这不是覆盖自带模板的最佳方式。
   ```

7. dbshell不好使，待解决

   ```
   完成了models部分，但是dbshell会报错，猜测是基于windows的原因，待解决
   ```

8. 关于models中的`Charfied`字段的`max_lenght`的问题（mysql5.7）

   ```
   Charfied对应的musql中是varchar
   max_lenght不是255，而是0~65535    #mysql5.7
   但是如果为这个字段设置了unique=True时的默认长度才会变为255
   顺便区分以下char/varchar/text:
   	char的长度为0~255，
   	varchar的最大长度是64K(65535),还要考虑not null占一位。不同的字符集的有效长度也不一样。例如utf-8的最多为21845。
   	text存储大文本，最长为4G
   从效率来说基本是char>varchar>text。但是如果使用Innodb引擎的话，推荐使用varchar代替char
   加一句，对于经常出现where语句中的字段，考虑加索引，整形的尤其适合加索引
   ```

9. 插播：防火墙管理：[防火墙管理.pdf](./docs/Centos7 防火墙管理 .pdf)

10. Python内置函数的整理，整理内容着重于网站开发方向。整理内容较为粗糙

11. admin.py中`save_mode`方法：

    ```
    	作用：通过给obj.owner赋值，就能达到自动设置owner的目的，request就是当前的请求，requests.user就是当前已登录的用户。如果是未登陆的情况下，通过request.user拿到的就是匿名用户对象。
    	obj是当前要保存的对象，而form是页面提交过来的表单之后的对象。change用于标志本次保存的数据是新增的还是更新的。
    	
    ```

12. django中admin.py的右侧自定义过滤器(让用户看到自己创建的分类)

    ```python
    SimpleListFilter
    SimpleListFilter中提供了两个供我们重写的方法。两个属性。
    	title用于展示标题，parameter_name就是查询时URL参数的名字，比如查询分类ID为1 的内容时，URL后面的Query部分是 》owner_category=1，此时就可以通过我们的过滤器拿到这个id,从而进行过滤。
        两个方法的作用如下：
        lookups：返回要展示的内容和查询用的id(就是上面的Query用的)
        queryset: 根据URL query的内容返回列表页数据。比如如果URL最后的query是？owner_category=1，那么这里拿到的self.value()也就是1，此时就会根据1来过滤Quesyset。这里的queryset是列表页所有展示数据的集合，即POST数据集
    ```

13. 自定义列表页数据只允许当前用户查看

    ```
    在相应的model注册中添加get_query自定义函数
    
    ```

14. 自定义编辑页面(数据录入页面)

    ```python
    在admin中添加以下内容
    
    fieldsets = (
    	(名称,{内容}),
        (名称,{内容}),
    )
    其中包含两个元素的tuple内容，第一个元素是当前板块的名称，第二个元素是当前板块的描述、字段和样式配置。
    总结为：
    	第一个元素是string,第二个元素是dict,而dict的keyt可以是'fields'、'description'、'classes。
        fields控制字段
        description控制描述
        classes的作用就是要给配置的板块加上一些CSS属性，django admin默认支持的是clooapse和wide,当然，自己也可以写一些其他属性，自己来处理样式
        还可以控制字段的展示方向：横向、纵向(针多对多字段）
        filter_horizontal=('tag',)
        filter_vertical=('tag',)
    ```

15. 自定义静态资源引入

    ```python
    我们可以通过自定义Media类来往页面上增加想要添加的js\css资源。
    ```

16. 自定义form

    ```python
    
    ```

17. 在同一页编辑关联数据

    ```python
    from django.contrib import admin
    class PostInline(admin.TabularInline):
        ...
        
    多用于相对字段内容较少的models.关联不关联的内容再议，感觉需求不大  
    ```

18. 定制site

    ```python
    定制site的作用在于：拥有两套后台地址，一套用来管理用户，一套用来管理业务。其实这两套系统都是基于一套逻辑的用户系统，只是我们在url上做了划分
    ```

19. 抽取admin基类，降低维护成本

    ```python
    
    ```

    

