from huggingface_hub import snapshot_download

# # Replace "lmsys/vicuna-7b-v1.5" with the exact model repo if different
# snapshot_download(
#     repo_id="lmsys/vicuna-7b-v1.5",
#     local_dir=r"C:\Users\dean0\OneDrive\Documents\GitHub\TravelUAV\Model\LLaMA-UAV\model_zoo",
#     # Set this to True if you want the folder to be cleared before each fresh download
#     # ignore_patterns=["*.lock"]  # or any pattern you wish to ignore
# )



# snapshot_download(
#     repo_id="wangxiangyu0814/llama-uav-7b",
#     local_dir=r"C:\Users\dean0\OneDrive\Documents\GitHub\TravelUAV\Model\LLaMA-UAV\work_dirs",
#     # Set this to True if you want the folder to be cleared before each fresh download
#     # ignore_patterns=["*.lock"]  # or any pattern you wish to ignore
# )

snapshot_download(
    repo_id="wangxiangyu0814/traveluav-traj-model",
    local_dir=r"C:\Users\dean0\OneDrive\Documents\GitHub\TravelUAV\Model\LLaMA-UAV\work_dirs\traj_predictor_bs_128_drop_0.1_lr_5e-4",
    # Set this to True if you want the folder to be cleared before each fresh download
    # ignore_patterns=["*.lock"]  # or any pattern you wish to ignore
)