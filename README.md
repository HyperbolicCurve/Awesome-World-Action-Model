<div align="center">

# 🤖 Awesome World Action Models

**📜 A Curated List of World Action Models, Vision-Language-Action (VLA), and Embodied AI Research**

![Awesome](https://awesome.re/badge.svg)
![Auto-updated](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/HyperbolicCurve/Awesome-World-Action-Model/main/.github/metrics.json&query=updated&label=Last%20Update&color=brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

</div>

## Overview

This repository aims to provide a comprehensive, curated, and continuously updated list of research papers, resources, and tools related to **World Action Models (WAM)**, **Vision-Language-Action (VLA)** models, and **Embodied AI**. The goal is to help researchers and engineers navigate the rapidly evolving field of robotics foundation models.

**World Action Models** are robotics policies that leverage world modeling capabilities—predicting future states—for action prediction. They represent a paradigm shift from reactive policies to predictive, world-aware decision-making.

**Vision-Language-Action (VLA)** models combine the rich language grounding and visual understanding of Vision-Language Models (VLMs) with action prediction, offering a scalable route toward general-purpose, language-conditioned robot policies.

## Table of Contents

- [Key Definitions](#key-definitions)
- [Comparison Methods & Baselines](#comparison-methods--baselines)
- [Surveys](#surveys)
- [VLA Models](#vla-models)
  - [General VLA](#general-vla)
  - [VLA with Reasoning](#vla-with-reasoning)
  - [VLA with 3D/4D Modeling](#vla-with-3d4d-modeling)
  - [Efficient VLA](#efficient-vla)
  - [VLA with RL Fine-tuning](#vla-with-rl-fine-tuning)
- [World Action Models](#world-action-models)
  - [WAM from Video Generation](#wam-from-video-generation)
  - [WAM from VLMs](#wam-from-vlms)
  - [WAM from Scratch](#wam-from-scratch)
- [Action Representations](#action-representations)
  - [Discrete Tokenization](#discrete-tokenization)
  - [Diffusion Policies](#diffusion-policies)
- [Robotics Policies](#robotics-policies)
- [Resources](#resources)
  - [Datasets](#datasets)
  - [Benchmarks](#benchmarks)
  - [Simulation Platforms](#simulation-platforms)
  - [Tools & Frameworks](#tools--frameworks)

---

## Comparison Methods & Baselines

<details>
<summary><b>📊 Click to expand baseline methods and complete paper list</b></summary>

### Quick Reference (from experimental tables)

| Category | Key Baselines |
|-----------|----------------|
| **VLA** | RT-1, RT-2, OpenVLA, Octo, π0, X-VLA, UniVLA, SmolVLA, VLANeXt |
| **Policy** | Diffusion Policy, ACT, BeT, PerAct, MVP, R3M, CQL, IQL |
| **World Model** | DreamerV1/V2/V3, I-JEPA, V-JEPA, DreamZero |

### Documentation

- 📋 [Complete Paper List](docs/all-papers.md) (129 papers, sorted newest first)
- 📊 [Baseline Methods](docs/baselines.md) (detailed comparison methods from experimental tables)

</details>

---

## 🆕 Latest Papers (Auto-updated)

> Papers are automatically fetched daily from arXiv. Last updated: 2026-03-31

### VLA

| Paper | Date | Code |
|-------|------|------|
| [DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA](https://arxiv.org/abs/2603.29844v1)<br><small>Yi Chen, Yuying Ge et al.</small> | 2026-03-31 |  |
| [FocusVLA: Focused Visual Utilization for Vision-Language-Action Models](https://arxiv.org/abs/2603.28740v1)<br><small>Yichi Zhang, Weihao Yuan et al.</small> | 2026-03-30 |  |
| [StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation](https://arxiv.org/abs/2603.28565v1)<br><small>Yiran Shi, Dongqi Guo et al.</small> | 2026-03-30 |  |
| [LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301v1)<br><small>Chanyoung Kim, Minwoo Kim et al.</small> | 2026-03-30 |  |
| [Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving](https://arxiv.org/abs/2603.27287v1)<br><small>Qiqi Liu, Huan Xu et al.</small> | 2026-03-28 |  |
| [VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation](https://arxiv.org/abs/2603.26666v1)<br><small>Zhide Zhong, Haodong Yan et al.</small> | 2026-03-27 |  |
| [Realtime-VLA V2: Learning to Run VLAs Fast, Smooth, and Accurate](https://arxiv.org/abs/2603.26360v1)<br><small>Chen Yang, Yucheng Hu et al.</small> | 2026-03-27 |  |
| [DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching](https://arxiv.org/abs/2603.26320v2)<br><small>Jiayi Chen, Wenxuan Song et al.</small> | 2026-03-27 |  |
| [Drive My Way: Preference Alignment of Vision-Language-Action Model for Personalized Driving](https://arxiv.org/abs/2603.25740v1)<br><small>Zehao Wang, Huaide Jiang et al.</small> | 2026-03-26 |  |
| [Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance](https://arxiv.org/abs/2603.25661v2)<br><small>Wenxuan Song, Jiayi Chen et al.</small> | 2026-03-26 |  |

### World Model

| Paper | Date | Code |
|-------|------|------|
| [Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.24581v1)<br><small>Linbo Wang, Yupeng Zheng et al.</small> | 2026-03-25 |  |
| [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666v2)<br><small>Tianyuan Yuan, Zibin Dong et al.</small> | 2026-03-17 |  |
| [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922v1)<br><small>Seonghyeon Ye, Yunhao Ge et al.</small> | 2026-02-17 |  |
| [Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998v2)<br><small>Lin Li, Qihang Zhang et al.</small> | 2026-01-29 |  |
| [STORM: Search-Guided Generative World Models for Robotic Manipulation](https://arxiv.org/abs/2512.18477v1)<br><small>Wenjun Lin, Jensen Zhang et al.</small> | 2025-12-20 |  |
| [Dynamic Sparsity: Challenging Common Sparsity Assumptions for Learning World Models in Robotic Reinforcement Learning Benchmarks](https://arxiv.org/abs/2511.08086v2)<br><small>Muthukumar Pandaram, Jakob Hollenstein et al.</small> | 2025-11-11 |  |
| [Ctrl-World: A Controllable Generative World Model for Robot Manipulation](https://arxiv.org/abs/2510.10125v3)<br><small>Yanjiang Guo, Lucy Xiaoyang Shi et al.</small> | 2025-10-11 |  |
| [iMoWM: Taming Interactive Multi-Modal World Model for Robotic Manipulation](https://arxiv.org/abs/2510.09036v1)<br><small>Chuanrui Zhang, Zhengxian Wu et al.</small> | 2025-10-10 |  |
| [WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation](https://arxiv.org/abs/2510.07313v1)<br><small>Zezhong Qian, Xiaowei Chi et al.</small> | 2025-10-08 |  |
| [GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://arxiv.org/abs/2508.17600v2)<br><small>Guanxing Lu, Baoxiong Jia et al.</small> | 2025-08-25 |  |

### Policy

| Paper | Date | Code |
|-------|------|------|
| [Enhancing Policy Learning with World-Action Model](https://arxiv.org/abs/2603.28955v1)<br><small>Yuci Han, Alper Yilmaz</small> | 2026-03-30 |  |
| [GigaWorld-Policy: An Efficient Action-Centered World--Action Model](https://arxiv.org/abs/2603.17240v2)<br><small>Angen Ye, Boyuan Wang et al.</small> | 2026-03-18 |  |

---


## Key Definitions

### Vision-Language-Action (VLA) Models

VLA models are robotics policies that inherit the pretrained VLMs' rich language grounding and visual understanding abilities to offer a scalable route toward general-purpose, language-conditioned robot policies.

**Key Paper:** [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) | Brohan et al. (2023) | [Project](https://robotics-transformer2.github.io)

### World Action Models (WAM)

WAM models are robotics policies that leverage the world modeling capability (i.e., predicting future states) for action prediction.

**Key Paper:** [DreamZero: World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) | Chen et al. (2026) | [Project](https://dreamzero0.github.io)

> **Note:** There is an intersection between VLA and WAM: WAMs built upon pretrained VLMs are simultaneously both VLA and WAM.

---

## Surveys

| Title | Authors | Year | Links |
|-------|---------|------|-------|
| Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges | Applied AI Research Lab | 2025 | [arXiv](https://arxiv.org/abs/2505.04769) |
| A Survey on Vision-Language-Action Models for Embodied AI | Ma et al. | 2024 | [arXiv](https://arxiv.org/abs/2405.14093) |
| Foundation Models for Embodied AI | Driess et al. | 2024 | [arXiv](https://arxiv.org/abs/2407.21200) |

---

## VLA Models

### General VLA

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **AC2-VLA**: Action-Context-Aware Adaptive Computation in VLA | Yu et al. | 2026 | [arXiv](https://arxiv.org/abs/2601.19634) |
| 2 | **APPLV**: Adaptive Planner Parameter Learning from VLA | Lu et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.08862) |
| 3 | **Act, Think or Abstain**: Complexity-Aware Adaptive Inference for VLA | Izzo et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.05147) |
| 4 | **AnyCamVLA**: Zero-Shot Camera Adaptation for Viewpoint Robust VLA | Heo et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.05868) |
| 5 | **CLARE**: Continuous Learning for VLA via Adapter Routing | Römer et al. | 2026 | [arXiv](https://arxiv.org/abs/2601.09512) |
| 6 | **DIAL**: Decoupling Intent and Action via Latent World Modeling for VLA | Chen et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.29844) |
| 7 | **EAPruning**: Adaptive Pruning with Interleaved Inference for VLA | Huang et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.00780) |
| 8 | **ETA-VLA**: Efficient Token Adaptation | Wang et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.25766) |
| 9 | **FAVLA**: Force-Adaptive Fast-Slow VLA | Li et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.23648) |
| 10 | **HarvestFlex**: Harvesting via VLA Policy Adaptation | Zhao et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.05982) |
| 11 | **On-the-Fly VLA**: VLA Adaptation via Test-Time RL | Liu et al. | 2026 | [arXiv](https://arxiv.org/abs/2601.06748) |
| 12 | **ProbeFlow**: Training-Free Adaptive Flow Matching for VLA | Fang et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.17850) |
| 13 | **RAFT**: Adapting VLA Models via Force-aware Curriculum | Zhang et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.12532) |
| 14 | **ROBOGATE**: Adaptive Failure Discovery for Safe Robot Policy | Kim et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.22126) |
| 15 | **SAMoE-VLA**: Scene Adaptive Mixture-of-Experts VLA | You et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.08113) |
| 16 | **SCALE**: Self-Uncertainty Adaptive Looking for VLA | Choi et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.04208) |
| 17 | **SOMA**: Memory-Augmented System for VLA Robustness | Li et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.24060) |
| 18 | **VGAS**: Adaptive Capacity Allocation for VLA | Kim et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.07404) |
| 19 | **VLA-Acceleration**: Accelerate VLA through Visual Token Caching | Wei et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.00686) |
| 20 | **VGAS**: Value-Guided Action-Chunk Selection for VLA | Xu et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.07399) |
| 21 | **VLANeXt**: Recipes for Building Strong VLA Models | Liu et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.18532) [Project](https://dravenalg.github.io/VLANeXt/) |
| 22 | **HoloBrain-0**: Technical Report | Horizon Robotics | 2026 | [arXiv](https://arxiv.org/abs/2602.12062) [Project](https://horizonrobotics.github.io/robot_lab/holobrain/) |
| 23 | **FocusVLA**: Focused Visual Utilization for VLA Models | Zhang et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.28740) |
| 24 | **StreamingVLA**: Streaming VLA with Action Flow Matching | Shi et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.28565) |
| 25 | **ABot-M0**: VLA with Action Manifold Learning | AMAP CVLab | 2026 | [arXiv](https://arxiv.org/abs/2602.11236) [Project](https://amap-cvlab.github.io/ABot-Manipulation/) |
| 26 | **SimVLA**: A Simple VLA Baseline for Robotic Manipulation | FrontierRoBo | 2026 | [arXiv](https://arxiv.org/abs/2602.18224) [Project](https://frontierrobo.github.io/SimVLA/) |
| 27 | **Lingbot-VLA**: A Pragmatic VLA Foundation Model | Robbyant | 2026 | [arXiv](https://arxiv.org/abs/2601.18692) [Project](https://technology.robbyant.com/lingbot-vla/) |
| 28 | **AC-DiT**: AC-DiT: Adaptive Coordination Diffusion Transformer | Chen et al. | 2025 | [arXiv](https://arxiv.org/abs/2507.01961) |
| 29 | **U-DiT**: U-DiT: U-shaped Diffusion Transformers | Wu et al. | 2025 | [arXiv](https://arxiv.org/abs/2509.24579) |
| 30 | **VLA-Adapter**: VLA-Adapter: Tiny-Scale VLA Paradigm | Wang et al. | 2025 | [arXiv](https://arxiv.org/abs/2509.09372) |
| 31 | **Gemini Robotics**: Bringing AI into the Physical World | DeepMind | 2025 | [arXiv](https://arxiv.org/abs/2503.20020) [Project](https://deepmind.google/models/gemini-robotics/) |
| 32 | **π\*0.6**: A VLA That Learns From Experience | Black et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.14759) [Project](https://www.pi.website/blog/pistar06) |
| 33 | **X-VLA**: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA | Zheng et al. | 2025 | [arXiv](https://arxiv.org/abs/2510.10274) [Project](https://thu-air-dream.github.io/X-VLA/) |
| 34 | **UniVLA**: Unified Vision-Language-Action Model | Wu et al. | 2025 | [arXiv](https://arxiv.org/abs/2506.19850) [Project](https://robertwyq.github.io/univla.github.io/) |
| 35 | **SmolVLA**: A VLA for Affordable and Efficient Robotics | LeRobot | 2025 | [arXiv](https://arxiv.org/abs/2506.01844) [Project](https://github.com/huggingface/lerobot) |
| 36 | **NORA**: A Small Open-Sourced Generalist VLA | Nandan et al. | 2025 | [arXiv](https://arxiv.org/abs/2504.19854) [Project](https://declare-lab.github.io/nora) |
| 37 | **VLA-0**: Building State-of-the-Art VLAs with Zero Modification | VLA0 | 2025 | [arXiv](https://arxiv.org/abs/2510.13054) [Project](https://vla0.github.io) |
| 38 | **CronusVLA**: Efficient Multi-Frame VLA | Li et al. | 2025 | [arXiv](https://arxiv.org/abs/2506.19816) [Project](https://lihaohn.github.io/CronusVLA.github.io/) |
| 39 | **OpenVLA-OFT**: Fine-Tuning VLAs: Optimizing Speed and Success | Lee et al. | 2025 | [arXiv](https://arxiv.org/abs/2502.19645) [Project](https://openvla-oft.github.io) |
| 40 | **AsyncVLA**: Asynchronous Flow Matching for VLA | Jiang et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.14148) [Project](https://github.com/YuhuaJiang2002/AsyncVLA) |
| 41 | **AVA-VLA**: VLA with Active Visual Attention | Li et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.18960) |
| 42 | **A-VL**: Adaptive Attention for Large VLA | Zhang et al. | 2024 | [arXiv](https://arxiv.org/abs/2409.14846) |
| 43 | **ADEM-VL**: Adaptive and Embedded Fusion for VLA | Hao et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.17779) |
| 44 | **OpenVLA**: OpenVLA: An Open-Source Vision-Language-Action Model | Kim et al. | 2024 | [arXiv](https://arxiv.org/abs/2406.09246) [Project](https://openvla.github.io) |
| 45 | **Octo**: Octo: An Open-Source Generalist Robot Policy | Ghosh et al. | 2024 | [arXiv](https://arxiv.org/abs/2405.12213) [Project](https://octo-models.github.io) |
| 46 | **π0**: A Multimodal Autoregressive Action Model | Black et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.24164) [Project](https://www.pi.website/blog/p0) |
| 47 | **RT-2**: Vision-Language-Action Models | Brohan et al. | 2023 | [arXiv](https://arxiv.org/abs/2307.15818) [Project](https://robotics-transformer2.github.io) |
| 48 | **RT-1**: Robotics Transformer for Real-World Control at Scale | Brohan et al. | 2022 | [arXiv](https://arxiv.org/abs/2212.06817) [Project](https://robotics-transformer1.github.io) |
| 49 | **VL-Adapter**: VL-Adapter: Parameter-Efficient Transfer Learning | Sung et al. | 2021 | [arXiv](https://arxiv.org/abs/2112.06825) |

### VLA with Reasoning

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **ACoT-VLA**: Action Chain-of-Thought for VLA Models | AgibotTech | 2026 | [arXiv](https://arxiv.org/abs/2601.11404) [Project](https://github.com/AgibotTech/ACoT-VLA) |
| 2 | **Fast-ThinkAct**: Efficient Vision-Language-Action Reasoning | Chen et al. | 2026 | [arXiv](https://arxiv.org/abs/2601.09708) |
| 3 | **CoT-VLA**: Visual Chain-of-Thought Reasoning for VLA | Chen et al. | 2025 | [arXiv](https://arxiv.org/abs/2503.22020) |
| 4 | **ThinkAct**: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning | Chen et al. | 2025 | [arXiv](https://arxiv.org/abs/2507.16815) |
| 5 | **UniVLA**: VLA with World Model | Wu et al. | 2025 | [arXiv](https://arxiv.org/abs/2506.19850) |

### VLA with 3D/4D Modeling

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **3D-VLA**: A 3D Vision-Language-Action Generative World Model | Chen et al. | 2024 | [arXiv](https://arxiv.org/abs/2403.09631) |
| 2 | **VoxPoser**: 3D-Aware VLA | Huang et al. | 2023 | [arXiv](https://arxiv.org/abs/2307.05973) [Project](https://voxposer.github.io) |

### Efficient VLA

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **FASTER**: Rethinking Real-Time Flow VLAs | Liu et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.19199) |
| 2 | **SmolVLA**: A Vision-Language-Action Model for Affordable Robotics | LeRobot | 2025 | [arXiv](https://arxiv.org/abs/2506.01844) |
| 3 | **AsyncVLA**: Asynchronous Flow Matching for VLA | Jiang et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.14148) [Project](https://github.com/YuhuaJiang2002/AsyncVLA) |
| 4 | **OpenHelix**: A Short Survey and Open-Source Dual-System VLA | Google DeepMind | 2025 | [arXiv](https://arxiv.org/abs/2505.03912) |
| 5 | **RTC**: Running VLAs at Real-time Speed | Google DeepMind | 2025 | [arXiv](https://arxiv.org/abs/2510.26742) |
| 6 | **AVA-VLA**: VLA with Active Visual Attention | Li et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.18960) |

### VLA with RL Fine-tuning

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **SimpleVLA-RL**: Scaling VLA Training via Reinforcement Learning | Pi Team | 2025 | [arXiv](https://arxiv.org/abs/2509.09674) |
| 2 | **OpenVLA-OFT**: Fine-Tuning VLAs: Optimizing Speed and Success | Lee et al. | 2025 | [arXiv](https://arxiv.org/abs/2502.19645) [Project](https://openvla-oft.github.io) |

### WAM from Video Generation

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **DreamZero**: World Action Models are Zero-shot Policies | Chen et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.15922) [Project](https://dreamzero0.github.io) |
| 2 | **DiT4DiT**: Jointly Modeling Video Dynamics and Actions | Ma et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.10448) |
| 3 | **Cosmos Policy**: Fine-Tuning Video Models for Visuomotor Control and Planning | NVIDIA | 2026 | [arXiv](https://arxiv.org/abs/2601.16163) [Project](https://developer.nvidia.com/cosmos) |
| 4 | **Video2Act**: A Dual-System Video Diffusion Policy | Sun et al. | 2025 | [arXiv](https://arxiv.org/abs/2512.03044) |

### WAM from VLMs

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **Goal-VLA**: Image-Generative VLMs as Object-Centric World Models Empower VLA | Lee et al. | 2025 | [arXiv](https://arxiv.org/abs/2506.23919) |

### WAM from Scratch

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **V-JEPA**: Video Joint-Embedding Predictive Architecture | Esser et al. | 2024 | [arXiv](https://arxiv.org/abs/2402.05883) |
| 2 | **DreamerV3**: Mastering Atari from Pixels | Hafner et al. | 2023 | [arXiv](https://arxiv.org/abs/2301.04104) [Project](https://github.com/danijar/dreamer) |
| 3 | **I-JEPA**: Image-based Joint-Embedding Predictive Architecture | Esser et al. | 2023 | [arXiv](https://arxiv.org/abs/2301.08243) |

## Action Representations

### Discrete Tokenization

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **Behavior Transformers (BeT)**: Multimodal Action Discretization | Shafiullah et al. | 2022 | [arXiv](https://arxiv.org/abs/2206.11251) |
| 2 | **Action Bins**: Discretizing Continuous Actions | Brohan et al. | 2023 | [arXiv](https://arxiv.org/abs/2307.15818) |
| 3 | **Action Tokens**: Learning Discrete Action Spaces | Chi et al. | 2023 | [arXiv](https://arxiv.org/abs/2303.04137) |

### Diffusion Policies

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **Diffusion Policy**: Diffusion for Robot Control | Chi et al. | 2023 | [arXiv](https://arxiv.org/abs/2303.04137) [Project](https://diffusion-policy.cs.columbia.edu) |
| 2 | **ACT/ALOHA**: Action Chunking Transformer | Zhao et al. | 2023 | [arXiv](https://arxiv.org/abs/2304.13705) [Project](https://aloha.ai) |
| 3 | **Flow Matching Policy**: Flow Matching for Action Generation | Zhou et al. | 2024 | [arXiv](https://arxiv.org/abs/2408.11039) [Project](https://github.com/facebookresearch/flow_matching) |
| 4 | **Transfusion**: AR + Diffusion in One Transformer | Zhou et al. | 2024 | [arXiv](https://arxiv.org/abs/2408.11039) |

---

## Robotics Policies

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **RT-1**: Robotics Transformer for Real-World Control | Brohan et al. | 2022 | [arXiv](https://arxiv.org/abs/2212.06817) [Code](https://github.com/google-research/robotics_transformer) |
| 2 | **Diffusion Policy**: Diffusion for Robot Control | Chi et al. | 2023 | [arXiv](https://arxiv.org/abs/2303.04137) |
| 3 | **ACT/ALOHA**: Action Chunking Transformer | Zhao et al. | 2023 | [arXiv](https://arxiv.org/abs/2304.13705) |
| 4 | **Behavior Transformers (BeT)**: Multimodal Action | Shafiullah et al. | 2022 | [arXiv](https://arxiv.org/abs/2206.11251) |
| 5 | **PerAct**: Behavior Primitive Discovery | Nasiriany et al. | 2023 | [arXiv](https://arxiv.org/abs/2210.03366) |

---

## Resources

### Datasets

| Name | Description | Size | Links |
|------|-------------|------|-------|
| **OXE** | Open X-Embodiment Dataset | 500k+ episodes | [Project](https://robotics-transformer-x.github.io) |
| **RT-1 Dataset** | Real Robot Manipulation | 130k episodes | [Project](https://robotics-transformer1.github.io) |
| **BridgeData** | Robot Learning Dataset | 70k episodes | [Project](https://rail.berkeley.edu/bridge_data) |
| **ALOHA** | Bimanual Manipulation | 10k+ episodes | [Project](https://aloha.ai) |
| **AgiBot World** | Large-scale Robot Dataset | 1M+ episodes | [Project](https://www.agibot-world.com) |
| **UMI** | Unified Manipulation Interface | 15k episodes | [Project](https://umisystem.github.io) |
| **DROID** | Dataset for Robot Imitation | 80k episodes | [Project](https://droid-dataset.github.io) |

### Benchmarks

| Name | Description | Links |
|------|-------------|-------|
| **Libero** | Modular Benchmark for Robot Learning | [Project](https://libero-project.github.io) |
| **RLBench** | Real Robot Benchmark | [Project](https://www.roboticbenchmark.org/rlbench) |
| **ManiSkill** | Generalizable Manipulation | [Project](https://maniskill.github.io) |
| **CALVIN** | Language-conditioned Manipulation | [Project](https://calvin.cs.uni-freiburg.de) |
| **RoboNet** | Large-scale Robot Dataset | [Project](https://robonet.cs.berkeley.edu) |
| **Metaworld** | Multi-task Benchmark | [Project](https://www.metaworldrl.org) |

### Simulation Platforms

| Name | Description | Links |
|------|-------------|-------|
| **Isaac Gym** | NVIDIA GPU-accelerated Physics | [Project](https://developer.nvidia.com/isaac-gym) |
| **Isaac Lab** | Robot Learning Framework | [Project](https://isaac-sim.github.io/IsaacLab) |
| **Gazebo** | Classic Robot Simulator | [Project](https://gazebosim.org) |
| **Mujoco** | Physics Engine | [Project](https://mujoco.org) |
| **PyBullet** | Physics Simulation | [Project](https://pybullet.org) |
| **Habitat** | Embodied AI Simulation | [Project](https://aihabitat.org) |
| **iGibson** | Interactive Gibson Environment | [Project](https://svl.stanford.edu/igibson) |

### Tools & Frameworks

| Name | Description | Links |
|------|-------------|-------|
| **LeRobot** | Hugging Face Robotics Framework | [Project](https://github.com/huggingface/lerobot) |
| **PyRobot** | Robotics Learning Framework | [Project](https://pyrobot.org) |
| **Robomimic** | Imitation Learning Framework | [Project](https://robomimic.github.io) |
| **OmniGibson** | Sim2Real Platform | [Project](https://behavior.stanford.edu/omnigibson) |
| **ManiSkill2** | Manipulation Benchmark | [Project](https://github.com/haosulab/ManiSkill2) |

---

## Contributing

Contributions are welcome! This repository uses automated tools for paper discovery:

1. **Add a paper**: Edit the README directly or open an issue
2. **Fix errors**: Submit a PR with corrections
3. **Suggest improvements**: Open an issue with your ideas

To run the paper scraper locally:
```bash
pip install -r requirements.txt
python scripts/arxiv_scraper.py --max-results 100 --days-back 180
```

## License

This repository is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by [awesome-vla-wam](https://github.com/DravenALG/awesome-vla-wam.git)
- Inspired by [awesome-physical-ai](https://github.com/keon/awesome-physical-ai.git)
- Inspired by [awesome-vla-study](https://github.com/MilkClouds/awesome-vla-study.git)

---

<div align="center">
<b>If you find this repository useful, please consider giving it a ⭐</b>
</div>
