---
name: jingmai-vertical-storyboard
description: 为国内或海外竖屏短剧做剧本诊断、导演方案、Seedance分段、专业连续分镜与局部修订；适用于动作、特效、文戏和镜头语言需联合设计的任务，不负责资产生图。
---

# 镜脉竖屏分镜导演

把剧本事实展开为有表演、有动作因果、有特效物理逻辑、可衔接的竖屏镜头。用户提供的剧本是事实源；本文与参考文件是工作方法。先判断观众需要看见的变化，再从摄影、光声、动作和特效词库中选有效手段。示例人物、招式、技能和影片设定不得带入剧本。

## 工作顺序

1. 按 [workflow.md](references/workflow.md) 读取指定剧本及必要的相邻集，核对集数、场次、对白、人物、道具、伤势和能力边界。先诊断逐场可优化机会，再给2—3种真正不同的导演方案。用户已选方案时直接继承，不重问。
2. 在正式分镜前，把方案写成可检验的“导演执行卡”：观众跟随谁、信息何时揭示、表演方向、动作体系、特效材质、摄影和剪辑节奏、禁止的误用。按 [director-plan-compiler.md](references/director-plan-compiler.md) 执行；不能只在摘要写方案名。逐场按 [narrative-shot-selection.md](references/narrative-shot-selection.md) 把剧情变化转成观看任务，再决定镜头职责。
3. 确认尚未确定的集数、国内/海外方向、Seedance 2.0/2.5、本集重点与Part数。用户明确决定的项目不重问；沉默不算确认。已明确授权生成时，按锁定事实执行。
4. 按 [pacing-and-shot-density.md](references/pacing-and-shot-density.md) 先列必需动作、对白和反应，再规划Part容量。工作流上限：2.0每Part不超过15秒，2.5每Part不超过30秒；实际接口更低时从严。这是制作约束，不是官方能力承诺。
5. 逐镜设计先读 [cinematic-language.md](references/cinematic-language.md) 的联合选择原则；确实需要运镜选择时读 [camera-movement-lexicon.md](references/camera-movement-lexicon.md)，需要关系、景别或角度时读 [shot-size-angle-composition.md](references/shot-size-angle-composition.md)，需要焦点、光影或声音调度时读 [focus-light-sound.md](references/focus-light-sound.md)。文戏读 [performance-direction.md](references/performance-direction.md)；打斗与追逐读 [action-choreography.md](references/action-choreography.md)，仅在需要武术词汇时读 [martial-arts-vocabulary.md](references/martial-arts-vocabulary.md)；特效读 [vfx-design.md](references/vfx-design.md)。同场混合戏同时满足相应模块，不能让特效遮掉攻防。若两套拍法仍难区分，可看 [method-examples.md](references/method-examples.md)，示例不能移植为剧情。
6. 用 [output-contract.md](references/output-contract.md) 交付，每镜只有标题、画面与表演、台词、环境音效、衔接五项。按 [quality-gates.md](references/quality-gates.md) 和 [counterfactual-tests.md](references/counterfactual-tests.md) 复核镜头是否真的服务故事；发现问题修最小范围。
7. 用户反馈时读 [directing-and-revision.md](references/directing-and-revision.md)，把“不够狠、乱、廉价、慢、平”等感受定位到具体镜头与原因，只改授权范围和必要衔接。

## 不可漂移的事实

- 保留原人物关系、事件顺序、全部对白原文与说话人、关键行动、能力和伤势边界、结果。分清对白、OS/VO、表演括号和阅读译文。未经授权不改剧情或台词。
- 专业术语只能辅助表达。每个入选术语必须附可见的脚步、身体、机位、材质、接触或空间结果；删除术语后镜头仍能执行。没有剧本依据时，不给人物冠以八卦掌等门派身份，也不添加新招式名、武器、能力或破坏。
- 一个Part是一个能自然完成的戏剧单元；每Part从镜头1编号，不写逐镜秒数。镜头数以职责和容量决定，不能机械凑数，也不能把多段攻防压成一句。
- 前景、移焦、特殊视角、变速和重点光影只在改变信息、关系或动作可读性时使用。每个镜头保持一个主要运镜。关键接触和受力必须可见。
- 已完成集与已认可镜头锁定。跨集和跨Part记住人物位置、朝向、持物、伤势、光源、声场和未完成动作；局部返修只调整相关镜头及必要接点。

## 可移植模板

`references/` 中的导演知识与固定输出契约是独立模板V9.0的正文来源。修改这些规则后，运行 `scripts/build_portable_template.py --output <目标Markdown路径>` 重新生成模板；不要维护另一份会漂移的规则副本。`scripts/validate_storyboard.py` 只能检查结构、编号和声明时长，不能代替人工判断剧情忠实度与镜头质量。
