# JWT의 대하여 알아보자
## 1. 소개
JWT(JSON Web Token)은 JSON을 사용하여 정보를 안전하게 전달하는 개방형 표준 방식이다.<br>
JWT는 Token에 정보를 저장하고 있으며, JWS(JSON Web Signature) 와 JWE(JSON Web Encryption)을 뜻한다.<br>
기술적인 정의는 서명되지 않은 클래임의 집합이다.

## JWS
JWS는 정보를 서버의 private key로 서명하여 토큰화 한 것 이다.<br>
header, payload, signature 로 이루어져 잇다.

#### header



#### signature
header의 표기된 알고리즘으로 private key를 사용하여 서명한 것이다.