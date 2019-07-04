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