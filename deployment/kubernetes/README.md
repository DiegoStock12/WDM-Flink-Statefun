# Deploy on Kubernetes

1) Make sure you created a Kubernetes cluster in Google Cloud Console. 
2) Add instances to this cluster. For these instances you're actually charged, so make sure you remove them when not used. The `Add node pool` will help you out. This option can be found in the cluster overview in your Google Cloud Console.
3) Install `kubectl` on your local pc.
4) Connect to your cluster. In the WebUI you can find the `Connect` button which will give you the right command.
It looks something like this `gcloud container clusters get-credentials CLUSTER_NAME --zone europe-west3-a --project PROJECT_NAME`.
You need `gcloud` installed and logged in using `gcloud login`. 
5) Verify it works by executing `kubectl get nodes`. It will show you the nodes in the cluster.
6) Apply manifests of all folders. `kubectl apply -f .`