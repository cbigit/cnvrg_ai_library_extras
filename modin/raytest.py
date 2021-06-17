import ray
ray.init(address="localhost:6379")

from cnvrgcallbak import CNVRGCallback

tracked_metrics = ['mean_accuracy']
analysis = tune.run(
    train_mnist,
    metric="mean_accuracy",
local_dir=".",
    mode="max",
    name="exp",
    scheduler=sched,
    stop={
        "mean_accuracy": 0.98,
        "training_iteration": 5
    },
    callbacks=[CNVRGCallback(tracked_metrics)],
    num_samples=5,
    config={
        "lr": tune.loguniform(1e-4, 1e-2),
        "momentum": tune.uniform(0.1, 0.9),
    })

