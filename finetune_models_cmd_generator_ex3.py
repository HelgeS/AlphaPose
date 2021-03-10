import os

cfgs = (
    (
        "configs/coco/resnet/256x192_res50_lr1e-3_2x-ski2dpose_no_cog.yaml",
        "coco_ski2dpose_no_cog_{}",
    ),  # COCO -> Ski2dpose
    (
        "configs/halpe_26/resnet/256x192_res50_lr1e-3_1x-ski2dpose_no_cog.yaml",
        "halpe26_ski2dpose_no_cog_{}",
    ),  # Halpe-26 -> Ski2dpose
    (
        "configs/halpe_136/resnet/256x192_res50_lr1e-3_1x-ski2dpose_no_cog.yaml",
        "halpe136_ski2dpose_no_cog_{}",
    ),  # Halpe-136 -> Ski2dpose
    (
        "configs/256x192_res50_lr1e-3_2x-ski2dpose_no_cog.yaml",
        "scratch_ski2dpose_no_cog_{}",
    ),  # None -> Ski2dpose
    (
        "configs/coco/resnet/256x192_res50_lr1e-3_2x-ski2dpose_with_cog.yaml",
        "coco_ski2dpose_with_cog_{}",
    ),  # COCO -> Ski2dpose
    (
        "configs/halpe_26/resnet/256x192_res50_lr1e-3_1x-ski2dpose_with_cog.yaml",
        "halpe26_ski2dpose_with_cog_{}",
    ),  # Halpe-26 -> Ski2dpose
    (
        "configs/halpe_136/resnet/256x192_res50_lr1e-3_1x-ski2dpose_with_cog.yaml",
        "halpe136_ski2dpose_with_cog_{}",
    ),  # Halpe-136 -> Ski2dpose
    (
        "configs/256x192_res50_lr1e-3_2x-ski2dpose_with_cog.yaml",
        "scratch_ski2dpose_with_cog_{}",
    ),  # None -> Ski2dpose
)

for i in range(1, 6):
    for cfg, exp_id_tmpl in cfgs:
        cfg_basename = os.path.basename(cfg)
        exp_id = exp_id_tmpl.format(i)
        print(
            f"""#!/bin/bash

#SBATCH --account=helge
#SBATCH --job-name={exp_id}
#SBATCH --output=exp/{exp_id}-{cfg_basename}/slurm.out
#SBATCH --partition dgx2q
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=03:00:00
#SBATCH --gres=gpu:1

srun conda run -n alphapose python scripts/train.py \
    --cfg {cfg} \
    --exp-id {exp_id}  \
    --nThreads 8 \
    --snapshot 5 \
    --board \
    --map \
    --detector efficientdet_d1""",
            file=open(exp_id + ".sh", "w"),
        )
