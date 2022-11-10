# Git command
---
## git init
##### 로컬 저장소(작업자의 PC에 설정된 Git 저장소)를 설정한다.

- #### git init
    >##### 현제 directory를 로컬 저장소로 설정한다.

- #### mkdir [<directory_name>]
    >##### make directory라고 생각하면 된다. directory_name의 이름을 가진 파일을 만든다
    
- #### cd [<directory_name>]
    >##### directory_name의 이름을 가진 directory로 이동한다.

## git status
##### 현재 작업 중인 파일의 상태를 확인한다.

- #### git init
    > ##### 현재 작업 중인 파일의 상태를 확인한다.

## git add 
##### 파일의 변경사항을 인덱스(staging area)에 추가한다.Git은 커밋하기 전, 인덱스에 먼저 커밋할 파일을 추가한다.

- #### git add [-A] [.]
    >##### 옵션 -A, .을 이용하여 전체 파일을 인덱스에 추가

- #### git add [<file_name>]
    >##### file_name의 이름을 가진 파일을 인덱스에 추가

## git commit
##### 인덱스에 추가된 변경 사항을 이력에 추가한다.
- #### git commit [-m <msg>]
    >##### msg의 문자열을 이력에 추가한다.

## git push
##### 로컬 저장소를 GitHub에 푸쉬한다. 커밋 목록이 그대로 복제되 옮겨진다.
- #### git remote add [<name(origin)>] [<url(git)>]
    >##### url에 나온 주소의 GitHub으로 커밋된 파일을 보낸다. name은 걍 origin으로 써라.

- #### git remote [-v]
    > ##### GitHub이 제대로 연결됬는지 확인할수있다.

- #### git push origin master
    >##### GitHub으로 보낸다. 드디어 끝났다.