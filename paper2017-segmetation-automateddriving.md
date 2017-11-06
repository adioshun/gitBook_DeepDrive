|논문명 |Deep Semantic Segmentation for Automated Driving: Taxonomy, Roadmap and Challenges |
| --- | --- |
| 저자\(소속\) | Mennatullah Siam \(\) |
| 학회/년도 | arXiv Jul 2017 ~ Aug 2017, [논문](https://arxiv.org/abs/1707.02432v2) |
| 키워드 | |
| 데이터셋(센서)/모델 | |
| 관련연구||
| 참고 | |
| 코드 | |

# Deep Semantic Segmentation for Automated Driving: Taxonomy, Roadmap and Challenges

In this paper, the semantic segmentation problem is explored from the perspective of automated driving. 

- 대부분의 세그멘테이션 알고리즘들은 **generic images**에 집중되어 있으며, **prior structure**를 활용하지 못하고 자율주행 차량을 목표로 하고 있지 않다. `Most of the current semantic segmentation algorithms are designed for generic images and do not incorporate prior structure and end goal for automated driving. `
    - 세그멘테이션 알고리즘 분류 `First,the paper begins with a generic taxonomic survey of semantic segmentation algorithms and then discusses how it fits in the context of automated driving. `
    - 정확도와 강건성 확보를 위한 **challenges **들 `Second, the particular challenges of deploying it into a safety system which needs high level of accuracy and robustness are listed. `
    - 다른 대안들 `Third, different alternatives instead of using an independent semantic segmentation module are explored. `
    - **CamVid** 데이터를 이용한 성늘 평가 `Finally, an empirical evaluation of various semantic segmentation architectures was performed on CamVid dataset interms of accuracy and speed.`


## I. INTRODUCTION

-  시멘틱 세그멘테이션은 아래 부분에서 연구 되었다. `It has been used in `
    - robotics [1][2][3][4]
    - medical applications [5][6]
    - augmented reality [7]
    - most prominently automated driving [8][9][10][11].
    
- 자율 주행에 대한 **두가지** 패러다임 `Two main paradigms for automated driving emerged: `
    - (1)인식 기반 접근법 `The mediated perception approach `
        - 장면 인식을 통해서 얻어진 정보를 컨트롤 할때 활용 `which parses the whole scene and uses this information for the control decision increasing the complexity and the cost of the system. `
    - (2)The behavior reflex paradigm 
        - 센서정보에 반응하는 컨트롤 결정을 맵핑하는 방식 `that relies more on end-to-end learning to map direct sensory input to driving decision `
        - which is an ill-posed problem due to the many possible ambiguous decisions, such as the work in [13][14]. 

- 하지만 최근에 행동 유동성`(affordance)`지표를 이용하는 방법이 제안 되었다. ` However, in [15] an intermediate approach was suggested that learns affordance indicators for the driving scene. `
    - These indicators can then feedback on a simple controller for the final driving decision.
    
