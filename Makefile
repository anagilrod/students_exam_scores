init:
	poetry shell
	poetry install

run_app: init
	sh deploy/run_app.sh

docker_build:
	docker build --pull --rm -f "Dockerfile" -t studentsexamscores:latest "."

docker_run:
	docker run --rm -d -p 8000:8000/tcp studentsexamscores:latest

docker_build_run: docker_build docker_run

kubernetes_cluster: docker_build
	kind create cluster --name local-cluster --config kind-config.yaml
	kind load docker-image studentsexamscores:latest --name local-cluster
	kubectl apply -f deployment.yaml
	kubectl apply -f service.yaml
	kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.7/config/manifests/metallb-native.yaml

kind_status:
	kubectl get service students-exam-scores-service
	kubectl get deployment students-exam-scores-deployment

kind_pods:
	kubectl get pods

kind_describe_deployment:
	kubectl describe deployment students-exam-scores-deployment

kind_logs:
	kubectl logs -l app=students-exam-scores -n default

kind_get_events:
	kubectl get events

kind_delete_cluster:
	kind delete cluster --name local-cluster