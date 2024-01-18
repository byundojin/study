# JWT의 대하여 알아보자
## 1. 소개
JWT(JSON Web Token)은 JSON을 사용하여 정보를 안전하게 전달하는 개방형 표준 방식이다.<br>
JWT는 Token에 정보를 저장하고 있으며, JWS(JSON Web Signature) 와 JWE(JSON Web Encryption)을 뜻한다.<br>
기술적인 정의는 서명되지 않은 클래임의 집합이다.

## JWE
JWE는 정보를 서버의 publick key로 암호화 한 것 이다.

## JWS
JWS는 정보를 서버의 private key로 서명하여 토큰화 한 것 이다.<br>
header, payload, signature 로 이루어져 잇다.

#### header
JWS를 서명하기 위한 정보를 담는다.

#### payload
실질적인 정보가 들어간다. JWE로 암호화하여 넣는다.

claim
- iss -> 발급자
- aud -> 발급 대상자
- sub -> 토큰 대상자
- iat -> 토큰 발급 시간
- exp -> 토큰 만료 시간

ex)<br>
```json
{
    "iss":"dojins_app",
    "aud":["dojins_app_1","dojins_app_2","dojins_app_3"],
    "sub":"chul@gmail.com",
    "iat":"2024:01:18:06:53:17",
    "exp":"2024:01:18:06:58:17"
}
```


#### signature
header의 표기된 알고리즘으로 private key를 사용하여 서명한 것이다.

## JWE + JWS
JWE는 토큰의 기밀성을 JWS는 토큰의 무결성을 지킬 수 있다.<br>
그러니 둘이 같이 사용하면 기밀성과 무결성을 동시에 챙길 수 있게된다.

### 사용 방법
#### 발급
1. key pair를 생성한다.
2. 토큰의 payload를 publick key로 암호화 한다.
3. 암호화된 payload를 private key로 서명한다.
#### 검증
1. payload를 private key로 서명하여 signature를 비교한다.
2. payload를 private key로 복호화하여 정보를 확인한다.

#### 장점
이와 같이 행한다면 다양한 장점이 있다.
- 발급과 인증에 대한 권한을 분리할 수 있다.
- 정보의 기밀성을 지켜 보안을 높일 수 있다.