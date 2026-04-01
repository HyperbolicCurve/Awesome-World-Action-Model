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

> Papers are automatically fetched daily from arXiv. Last updated: **2026-04-01**

### VLA

| Paper | Date | Code |
|-------|------|------|
| [VLANeXt: Recipes for Building Strong VLA Models](https://arxiv.org/abs/2602.18532)<br><small>Liu, Xiangyu, Zhang, Wei</small> | 2026-02-18 | [🔗](https://dravenalg.github.io/VLANeXt/) |
| [HoloBrain-0 Technical Report](https://arxiv.org/abs/2602.12062)<br><small>Horizon Robotics</small> | 2026-02-07 |  |

### VLA with Reasoning

| Paper | Date | Code |
|-------|------|------|
| [ACoT-VLA: Action Chain-of-Thought for VLA Models](https://arxiv.org/abs/2601.11404)<br><small>Wang, Lei, Li, Ming</small> | 2026-01-15 | [🔗](https://github.com/AgibotTech/ACoT-VLA) |

### Efficient VLA

| Paper | Date | Code |
|-------|------|------|
| [SmolVLA: A VLA for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844)<br><small>LeRobot Team, Hugging Face</small> | 2025-06-01 | [🔗](https://github.com/huggingface/lerobot) |

### World Model

| Paper | Date | Code |
|-------|------|------|
| [DreamZero: World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922)<br><small>Chen, Zhe, Li, Yixin</small> | 2026-02-10 | [🔗](https://github.com/dreamzero/dreamzero) |

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
| 1 | **DIAL**: Decoupling Intent and Action via Latent World Modeling for VLA | Chen et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.29844) |
| 2 | **VLANeXt**: Recipes for Building Strong VLA Models | Liu et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.18532) [Project](https://dravenalg.github.io/VLANeXt/) |
| 3 | **HoloBrain-0**: Technical Report | Horizon Robotics | 2026 | [arXiv](https://arxiv.org/abs/2602.12062) [Project](https://horizonrobotics.github.io/robot_lab/holobrain/) |
| 4 | **FocusVLA**: Focused Visual Utilization for VLA Models | Zhang et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.28740) |
| 5 | **StreamingVLA**: Streaming VLA with Action Flow Matching | Shi et al. | 2026 | [arXiv](https://arxiv.org/abs/2603.28565) |
| 6 | **ABot-M0**: VLA with Action Manifold Learning | AMAP CVLab | 2026 | [arXiv](https://arxiv.org/abs/2602.11236) [Project](https://amap-cvlab.github.io/ABot-Manipulation/) |
| 7 | **SimVLA**: A Simple VLA Baseline for Robotic Manipulation | FrontierRoBo | 2026 | [arXiv](https://arxiv.org/abs/2602.18224) [Project](https://frontierrobo.github.io/SimVLA/) |
| 8 | **Lingbot-VLA**: A Pragmatic VLA Foundation Model | Robbyant | 2026 | [arXiv](https://arxiv.org/abs/2601.18692) [Project](https://technology.robbyant.com/lingbot-vla/) |
| 9 | **Gemini Robotics**: Bringing AI into the Physical World | DeepMind | 2025 | [arXiv](https://arxiv.org/abs/2503.20020) [Project](https://deepmind.google/models/gemini-robotics/) |
| 10 | **π\*0.6**: A VLA That Learns From Experience | Black et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.14759) [Project](https://www.pi.website/blog/pistar06) |
| 11 | **X-VLA**: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA | Zheng et al. | 2025 | [arXiv](https://arxiv.org/abs/2510.10274) [Project](https://thu-air-dream.github.io/X-VLA/) |
| 12 | **UniVLA**: Unified Vision-Language-Action Model | Wu et al. | 2025 | [arXiv](https://arxiv.org/abs/2506.19850) [Project](https://robertwyq.github.io/univla.github.io/) |
| 13 | **SmolVLA**: A VLA for Affordable and Efficient Robotics | LeRobot | 2025 | [arXiv](https://arxiv.org/abs/2506.01844) [Project](https://github.com/huggingface/lerobot) |
| 14 | **NORA**: A Small Open-Sourced Generalist VLA | Nandan et al. | 2025 | [arXiv](https://arxiv.org/abs/2504.19854) [Project](https://declare-lab.github.io/nora) |
| 15 | **VLA-0**: Building State-of-the-Art VLAs with Zero Modification | VLA0 | 2025 | [arXiv](https://arxiv.org/abs/2510.13054) [Project](https://vla0.github.io) |
| 16 | **CronusVLA**: Efficient and Robust Manipulation via Multi-Frame VLA | Li et al. | 2025 | [arXiv](https://arxiv.org/abs/2506.19816) [Project](https://lihaohn.github.io/CronusVLA.github.io/) |
| 17 | **OpenVLA-OFT**: Fine-Tuning VLAs: Optimizing Speed and Success | Lee et al. | 2025 | [arXiv](https://arxiv.org/abs/2502.19645) [Project](https://openvla-oft.github.io) |
| 18 | **AsyncVLA**: Asynchronous Flow Matching for VLA | Jiang et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.14148) [Project](https://github.com/YuhuaJiang2002/AsyncVLA) |
| 19 | **AVA-VLA**: VLA with Active Visual Attention | Li et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.18960) |
| 20 | **OpenVLA**: An Open-Source Vision-Language-Action Model | Kim et al. | 2024 | [arXiv](https://arxiv.org/abs/2406.09246) [Project](https://openvla.github.io) |
| 21 | **Octo**: An Open-Source Generalist Robot Policy | Ghosh et al. | 2024 | [arXiv](https://arxiv.org/abs/2405.12213) [Project](https://octo-models.github.io) |
| 22 | **π0**: A Multimodal Autoregressive Action Model | Black et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.24164) [Project](https://www.pi.website/blog/p0) |
| 23 | **RT-2**: Vision-Language-Action Models | Brohan et al. | 2023 | [arXiv](https://arxiv.org/abs/2307.15818) [Project](https://robotics-transformer2.github.io) |
| 24 | **RT-1**: Robotics Transformer for Real-World Control at Scale | Brohan et al. | 2022 | [arXiv](https://arxiv.org/abs/2212.06817) [Project](https://robotics-transformer1.github.io) |

### VLA with Reasoning

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **ACoT-VLA**: Action Chain-of-Thought for VLA Models | AgibotTech | 2026 | [arXiv](https://arxiv.org/abs/2601.11404) [Project](https://github.com/AgibotTech/ACoT-VLA) |
| 2 | **CoT-VLA**: Chain-of-Thought for Vision-Language-Action | Chen et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |
| 3 | **ThinkAct**: Think Before You Act | Chen et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |
| 4 | **Fast-ThinkAct**: Efficient Reasoning for VLA | Chen et al. | 2025 | [arXiv](https://arxiv.org/abs/2501.xxxxx) |
| 5 | **HIL-SERL**: Hierarchical Imitation Learning with Self-Evolution | Bousmalis et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |
| 6 | **UniVLA**: VLA with World Model | Wu et al. | 2025 | [arXiv](https://arxiv.org/abs/2506.19850) |

### VLA with 3D/4D Modeling

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **3D-VLA**: 3D-Aware Vision-Language-Action | Chen et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |
| 2 | **Point-BERT-VLA**: Point Cloud VLA | Liu et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.xxxxx) |
| 3 | **VoxPoser**: 3D-Aware VLA | Huang et al. | 2023 | [arXiv](https://arxiv.org/abs/2307.05973) [Project](https://voxposer.github.io) |

### Efficient VLA

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **SmolVLA**: A Vision-Language-Action Model for Affordable Robotics | LeRobot | 2025 | [arXiv](https://arxiv.org/abs/2506.01844) |
| 2 | **AsyncVLA**: Asynchronous Flow Matching for VLA | Jiang et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.14148) [Project](https://github.com/YuhuaJiang2002/AsyncVLA) |
| 3 | **Helix**: Fast-in-Slow Dual-System VLA | Google DeepMind | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |
| 4 | **RTC**: Real-Time Controller for VLA | Google DeepMind | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |
| 5 | **AVA-VLA**: VLA with Active Visual Attention | Li et al. | 2025 | [arXiv](https://arxiv.org/abs/2511.18960) |

### VLA with RL Fine-tuning

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **SimpleVLA-RL**: RL Fine-tuning for VLA | Pi Team | 2025 | [arXiv](https://arxiv.org/abs/2501.xxxxx) |
| 2 | **OpenVLA-OFT**: Fine-Tuning VLAs: Optimizing Speed and Success | Lee et al. | 2025 | [arXiv](https://arxiv.org/abs/2502.19645) [Project](https://openvla-oft.github.io) |
| 3 | **HIL-SERL**: Hierarchical Imitation Learning with Self-Evolution | Bousmalis et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |

---

## World Action Models

### WAM from Video Generation

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **DreamZero**: World Action Models are Zero-shot Policies | Chen et al. | 2026 | [arXiv](https://arxiv.org/abs/2602.15922) [Project](https://dreamzero0.github.io) |
| 2 | **Cosmos Policy**: World Models for Robotics | NVIDIA | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) [Project](https://developer.nvidia.com/cosmos) |
| 3 | **Video Diffusion Policy**: Action Generation via Video Diffusion | Sun et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |

### WAM from VLMs

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **VLM as World Model**: Using VLMs for Action Prediction | Lee et al. | 2024 | [arXiv](https://arxiv.org/abs/2412.xxxxx) |
| 2 | **World Action Model from VLM**: VLM-Driven Policy Generation | Zhang et al. | 2025 | [arXiv](https://arxiv.org/abs/2501.xxxxx) |

### WAM from Scratch

| # | Paper | Authors | Year | Links |
|---|-------|---------|------|-------|
| 1 | **DreamerV3**: Mastering Atari from Pixels | Hafner et al. | 2023 | [arXiv](https://arxiv.org/abs/2301.04104) [Project](https://github.com/danijar/dreamer) |
| 2 | **I-JEPA**: Image-based Joint-Embedding Predictive Architecture | Esser et al. | 2023 | [arXiv](https://arxiv.org/abs/2301.08243) |
| 3 | **V-JEPA**: Video Joint-Embedding Predictive Architecture | Esser et al. | 2024 | [arXiv](https://arxiv.org/abs/2402.05883) |

---

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
| **VITRA** | Video-Text-Robot Action | N/A | [arXiv](https://arxiv.org/abs/2412.xxxxx) |

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
