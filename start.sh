parentDir="$(dirname "$(pwd)")"
homeDir=$HOME

# Start KinD

cat <<EOF | kind create cluster --config=-
apiVersion: kind.x-k8s.io/v1alpha4
kind: Cluster
featureGates:
  "APIServerIdentity": true
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraMounts:
  - hostPath: $parentDir
    containerPath: /data
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    listenAddress: 127.0.0.1
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    listenAddress: 127.0.0.1
    protocol: TCP
  - containerPort: 30432
    hostPort: 30432
    listenAddress: 127.0.0.1
    protocol: TCP
EOF

kubectl cluster-info --context kind-kind

# Load Docker Images
kind load docker-image statyes-api statyes-client

# Load in the Secrets
kubectl create secret tls statyes-tls --key="$homeDir/.ssl/statyes.localhost+1-key.pem" --cert="$homeDir/.ssl/statyes.localhost+1.pem"

# Start Ingress
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml

sleep 20

# Start the Cluster
kubectl apply -f ./.kube