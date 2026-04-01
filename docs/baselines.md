# Comparison Methods & Baselines

This document contains baseline methods extracted from experimental tables of major VLA/WAM papers.

## VLA Baselines

| Method | Paper | Year | Description |
|---------|--------|------|-------------|
| **DIAL** | Decoupling Intent and Action via Latent World Modeling | 2026 | Intent-action decoupling with latent world modeling |
| **VLANeXt** | Recipes for Building Strong VLA Models | 2026 | VLA architecture recipes |
| **FocusVLA** | Focused Visual Utilization for VLA Models | 2026 | Focused visual attention in VLA |
| **StreamingVLA** | Streaming VLA with Action Flow Matching | 2026 | Streaming with flow matching |
| **ABot-M0** | VLA with Action Manifold Learning | 2026 | Action manifold learning |
| **SimVLA** | Simple VLA Baseline for Robotic Manipulation | 2026 | Simple VLA baseline |
| **Lingbot-VLA** | Pragmatic VLA Foundation Model | 2026 | Pragmatic VLA approach |
| **Gemini Robotics** | Bringing AI into the Physical World | 2025 | Gemini-based VLA |
| **π\*0.6** | A VLA That Learns From Experience | 2025 | Experience-learning VLA |
| **X-VLA** | Soft-Prompted Cross-Embodiment VLA | 2025 | Soft-prompted cross-embodiment |
| **UniVLA** | Unified Vision-Language-Action Model | 2025 | Unified VLA with world model |
| **SmolVLA** | VLA for Affordable and Efficient Robotics | 2025 | Compact VLA for edge devices |
| **NORA** | Small Open-Sourced Generalist VLA | 2025 | Small parameter VLA |
| **VLA-0** | Building State-of-the-Art VLAs with Zero Modification | 2025 | Zero-modification VLA |
| **CronusVLA** | Efficient Multi-Frame VLA | 2025 | Multi-frame VLA modeling |
| **OpenVLA-OFT** | Fine-Tuning VLAs: Optimizing Speed and Success | 2025 | Online fine-tuning |
| **AsyncVLA** | Asynchronous Flow Matching for VLA | 2025 | Asynchronous flow matching |
| **AVA-VLA** | VLA with Active Visual Attention | 2025 | Active visual attention |
| **OpenVLA** | An Open-Source VLA | 2024 | First open-source VLA |
| **Octo** | Open-Source Generalist Robot Policy | 2024 | Modular generalist policy |
| **π0** | Multimodal Autoregressive Action Model | 2024 | Flow matching + action expert |
| **RT-2** | Vision-Language-Action Models | 2023 | VLA paradigm establishment |
| **RT-2-55B** | Vision-Language-Action Models | 2023 | 55B parameter version |
| **RT-2-1B** | Vision-Language-Action Models | 2023 | 1B parameter version |
| **RT-1** | Robotics Transformer for Real-World Control | 2022 | First large-scale robotics transformer |
| **RT-1-35M** | Robotics Transformer for Real-World Control | 2022 | 35M parameter version |

## World Model Baselines

| Method | Paper | Year | Description |
|---------|--------|------|-------------|
| **DreamZero** | World Action Models are Zero-shot Policies | 2026 | World model as zero-shot policy |
| **HCLSM** | Hierarchical Causal Latent State Machines | 2026 | Hierarchical causal world model |
| **WAM** | World-Action Model | 2026 | Action-regularized world model |
| **DreamerV3** | Mastering Atari from Pixels | 2023 | World model RL algorithm |
| **DreamerV2** | Mastering Atari from Pixels | 2022 | Improved world model |
| **DreamerV1** | Learning Behaviors from Pixels | 2020 | Original world model |
| **I-JEPA** | Image-based Joint-Embedding Predictive Architecture | 2023 | Joint embedding predictive |
| **V-JEPA** | Video Joint-Embedding Predictive Architecture | 2024 | Video joint embedding |
| **Cosmos Policy** | World Models for Robotics | 2024 | NVIDIA world model policy |

## Policy Baselines

| Method | Paper | Year | Description |
|---------|--------|------|-------------|
| **Diffusion Policy** | Diffusion for Robot Control | 2023 | Diffusion model for action generation |
| **ACT** | Action Chunking Transformer | 2023 | CVAE-based action chunking |
| **ACT-ALOHA** | Action Chunking with ALOHA | 2023 | Bimanual manipulation |
| **BeT** | Behavior Transformers | 2022 | Multimodal action discretization |
| **PerAct** | Behavior Primitive Discovery | 2023 | Per-act primitive learning |
| **MVP** | Masked Visual Pre-training | 2022 | Masked visual encoder pretraining |
| **R3M** | Universal Visual Representation | 2022 | Self-supervised visual representation |
| **CQL** | Conservative Q-Learning | 2020 | Conservative offline RL |
| **IQL** | Implicit Q-Learning | 2021 | Implicit offline RL |

## Dataset Baselines

| Dataset | Source | Tasks | Size |
|----------|---------|-------|------|
| **OXE** | Open X-Embodiment | 547 | 500k+ episodes |
| **RT-1 Dataset** | Google Research | 9 | 130k episodes |
| **BridgeData** | Berkeley AI Research | 8 | 70k episodes |
| **ALOHA** | Stanford | 8 | 10k+ episodes |
| **AgiBot World** | Agibot | 100+ | 1M+ episodes |
| **UMI** | CMU | 6 | 15k episodes |
| **DROID** | CMU | 56 | 80k episodes |
| **Fractal** | Berkeley | 20 | 10M+ demonstrations |

## Benchmark Baselines

| Benchmark | Tasks | Evaluation Metric |
|-----------|--------|------------------|
| **Libero** | Object manipulation | Success rate |
| **Libero-Goal** | Goal-conditioned manipulation | Success rate |
| **Libero-Object** | Object manipulation | Success rate |
| **RLBench** | 100+ tasks | Success rate |
| **CALVIN** | Sequential manipulation | Success rate |
| **ManiSkill2** | Manipulation tasks | Success rate |
| **Metaworld** | 50 tasks | Success rate |

## Common Metrics

| Metric | Description |
|--------|-------------|
| **Success Rate** | Percentage of successfully completed tasks |
| **Average Return** | Cumulative reward over episodes |
| **Completion Rate** | Tasks completed within time limit |
| **Efficiency** | Time taken to complete tasks |
| **Robustness** | Performance across variations |
| **Generalization** | Performance on unseen tasks/objects |
| **Sim2Real Gap** | Performance drop from sim to real |
| **Inference Time** | Time per action prediction |
| **Throughput** | Actions per second |
