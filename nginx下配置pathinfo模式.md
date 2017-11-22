###nginx下配置pathinfo模式

> 首先tp5的访问目录指向到webroot/public文件夹中。
> thinkphp的url访问：http://serverName/index.php（或者其它应用入口文件）/模块/控制器/操作/[参数名/参数值...]，这个需要支持pathinfo，Apache默认支持，而Nginx不支持。
> 1.php.ini中的配置参数cgi.fix_pathinfo = 1
> 2.修改nginx.conf文件。

```

    location ~ \.php(.*)$ {
                fastcgi_pass   127.0.0.1:9000;
                fastcgi_index  index.php;
    #下面两句是给fastcgi权限，可以支持 ?s=/module/controller/action的url访问模式
                fastcgi_split_path_info  ^((?U).+\.php)(/?.+)$;
                fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    #下面两句才能真正支持 index.php/index/index/index的pathinfo模式
                fastcgi_param  PATH_INFO  $fastcgi_path_info;
                fastcgi_param  PATH_TRANSLATED  $document_root$fastcgi_path_info;
                include        fastcgi_params;
            }

复制代码
这样就能在linux,nginx环境下运行tp5了。

3. 去掉/index.php/
修改nginx.conf文件

    location / {
                index  index.html index.htm index.php;
                #autoindex  on;
                
              if (!-e $request_filename) {
                rewrite  ^(.*)$  /index.php?s=/$1  last;
                break;
              }
            }
            
            
            
            
            
            
```     
      
      
      
    lchat.conf配置如下
   ```
    server {
        charset utf-8;
        client_max_body_size 128M;
    
        listen 80; ## listen for ipv4
        #listen [::]:80 default_server ipv6only=on; ## listen for ipv6
    
        server_name www.chat.com;
        root        /www/lchat/public/;
        index       index.php index.html;
    
        access_log  /www/log/access.log;
        error_log   /www/log/error.log;
    
        location / {
            index  index.html index.htm index.php;
                #autoindex  on;
    
              if (!-e $request_filename) {
                rewrite  ^(.*)$  /index.php?s=/$1  last;
                break;
              }
            # Redirect everything that isn't a real file to index.php
            try_files $uri $uri/ /index.php$is_args$args;
        }
    
        # uncomment to avoid processing of calls to non-existing static files by Yii
        #location ~ \.(js|css|png|jpg|gif|swf|ico|pdf|mov|fla|zip|rar)$ {
        #    try_files $uri =404;
        #}
        #error_page 404 /404.html;
    
          location ~ \.php$ {
                fastcgi_pass   127.0.0.1:9000;
                fastcgi_index  index.php;
                #下面两句是给fastcgi权限，可以支持 ?s=/module/controller/action的url访问模式
                fastcgi_split_path_info  ^((?U).+\.php)(/?.+)$;
                fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
                #下面两句才能真正支持 index.php/index/index/index的pathinfo模式
                fastcgi_param  PATH_INFO  $fastcgi_path_info;
                fastcgi_param  PATH_TRANSLATED  $document_root$fastcgi_path_info;
                include        fastcgi_params;
    
            }
    
    
        location ~* /\. {
            deny all;
        }
    }
    ```
