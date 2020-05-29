
## pm2 / supervisor 

### pm2: 

 - install : `npm install -g pm2` (nodejs)
 
 - 美观，命令简单易用

 - 不建议使用 pm2-logrotate， 应该直接使用系统 logrotate 服务
 
 - pm2 <=3.2.3 `cluster` 模式行为无效
 
 - 配置文件： 相对 `pm2.json`, 更建议使用 `pm2.config.js`，方便自定义环境变量
 
```js
// -- pm2.config.js --
// pm2 start pm2.config.js
const project = __dirname.split('/').pop();
const path = __dirname + '/venv/bin:/bin:/usr/bin';

const local_app = {
  "name": project,
  "cwd": ".",
  "script": "manage.py",
  "args": "runserver",
  "interpreter": "./venv/bin/python",
  "env": {
    "PATH": path,
  },
  "env_production": {
    "NODE_ENV": "production"
  },
};

const gunicorn_wsgi = {
  "name": project,
  "cwd": ".",
  "script": "etc/run_gunicorn.sh",
  // "interpreter": "/bin/bash",
  "env": {
    "PATH": path,
  },
  "env_production": {
    "NODE_ENV": "production"
  },
  "out_file": "/dev/null"
};


module.exports = {
  apps: [
    local_app,
    gunicorn_wsgi,
  ],
};

```
 
 