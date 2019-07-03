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