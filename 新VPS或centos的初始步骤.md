1. python2没有pip

  ```shell
  yum -y install epel-release  #安装扩展源
  yum -y install python-pip
  ```

2. 安装python3

  ```shell
  yum -y groupinstall "Development tools"
  yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
  mkdir /usr/local/python3
  tar -xvJf Python-3.6.2.tar.xz
  cd Python-3.6.2
  ./configure --prefix=/usr/local/python3
  make && make install 
  
  ln -s /usr/local/python3/bin/python3 /usr/bin/python3
  ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
  
  pip3 install --upgrade pip
  pip3 install virtualenv
  
  ```

3. 安装nginx

  ```
  自定义安装：
  yum install gcc-c++
  yum install -y pcre pcre-devel
  yum install -y zlib zlib-devel
  wget -c https://nginx.org/download/nginx-1.10.1.tar.gz
  tar -zxvf nginx-1.10.1.tar.gz
  cd nginx-1.10.1
  ./configure
  make && make install
  
  
  简易安装(未经常使用)：
  yum install -y nginx
  systemctl enable nginx.service #设置开机启动
  systemctl start nginx.service  #启动
  此安装方式的nginx的配置文件位于/etc/nginx/nginx.conf
  ```

4. 防火墙(vps采用厂商的后台页面管理即可)

  ```
  firewall-cmd --zone=public --add-port=80/tcp --permanent 
  firewall-cmd --reload
  参考链接：
  	https://www.cnblogs.com/chrion/p/7327003.html
  ```

5. 修改python3 PIP源为阿里源

    ```
    pwd:/root
    mkdir .pip
    vi .pip/pip.conf
    ----
        [global]
        index-url=http://mirrors.aliyun.com/pypi/simple/
    
        [install]
        trusted-host=mirrors.aliyun.com
    ----
    ```

6. 更新centos7系统的sqlite3版本(django2.2.3版本不支持sqllite3.7)

    ```
    /usr/bin/sqlite3 --version
    3.7.17 2013-05-20 00:56:22 118a3b35693b134d56ebd780123b7fd6f1497668
    wget https://www.sqlite.org/2019/sqlite-autoconf-3270200.tar.gz[根据具体版本进行修改]
    tar -zxvf sqlite-autoconf-3270200.tar.gz
    ./configure --prefix=/usr/local
    make && make install
    检查新安装的版本：
    	/usr/local/bin/sqlite3 --version
    mv /usr/bin/sqlite3  /usr/bin/sqlite3_old
    export LD_LIBRARY_PATH="/usr/local/lib"  #设置开机启动
    source ~/.bashrc  #立即生效
    ```

    