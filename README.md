## atcoder_python
### Description
* Reproduction of python3 and pypy environment in atcoder on VSCode.
* The atcoder-cli and online-judge-tools for automated testing and submission.

## Assumption
The VS Code extension "Remote-Containers" is intended to be used.

### Usage
Clone this repository
 ```
 git clone https://github.com/gomatofu/atcoder_python.git
 ```
Open in VSCode
 ```
 code atcoder_python
 ```
Open the command palette on VSCode and select `Remote-Containers: Reopen in Container`.

Commands for question creation, automated testing, and automated testing are introduced at the following sites.
[atcoder-cli-command](http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/)

I have written more details on the community blog if you would like to take a look.
https://qiita.com/gomatofu/items/1adae9b7cd79b0f8044f
### atcoder_python

### ログイン
 oj login https://atcoder.jp/contests

 ### テストケースなどを取得
 acc new abc251

 ### PyPy3でのテスト実施
 alias test='oj t -c "pypy3 main.py" -d ./tests/'
 ### Pythonでのテスト実施
 alias test2='oj t -c "python3 main.py" -d ./tests/'

 ### PyPy3での解答提出
 alias sb='acc s main.py -- --guess-python-interpreter pypy'
 ### Pythonでの解答提出
 alias sb2='acc s main.py'

 ### コンテストフォルダへ移動
 alias c='cd contest'

 ### main.pyを開く
 alias o='code main.py'

 ### 出力確認用
 alias d='python main.py'

AtCoder Beginners Selectionの問題にpythonで解答
