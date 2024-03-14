### 环境

* conda配置相关
    * 删除配置 `conda config --remove-key channels --force`
    * 渠道查询 `conda config --show channels`
    * 渠道修改 `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main`

* conda环境相关
    * 环境查看 `conda info --envs`
    * 依赖包版本查看 `conda list numpy`
    * 搜索包版本 `conda search numpy --channel conda-forge`
    * conda python环境 `conda create -n env38 python=3.8`
    * 激活环境 `conda activate env38`
    * 删除依赖包 `conda remove python`
    * 常规依赖安装 `conda install numpy pytorch matplotlib pandas requests`
