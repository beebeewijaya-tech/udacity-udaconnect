## STEPS
1. on root directory
2. kubectl apply -f deployment
3. kubectl get svc
4. find `udaconnect-grpc-api-internal` change `GRPC_SERVER` to the IP from that cluster ip eg. 10.110.103.220
5. find `udaconnect-person-api` change `PERSON_HOST` to the IP from that nodeport cluster ip eg. 10.98.150.133
6. kubectl apply -f deployment
7. kubectl rollout restart deploy udaconnect-person-api
8. kubectl rollout restart deploy udaconnect-grpc-api
9. kubectl get pods
10. find `postgres` pods and do `sh scripts/run_db_command.sh postgres-5f676c995d-v96lh`
11. Run the kafka by following the deployment/kafka-installation
12. Run helm repo add bitnami https://charts.bitnami.com/bitnami
13. Run helm install kafka-release bitnami/kafka
14. Run kubectl run kafka-release-client --restart='Never' --image docker.io/bitnami/kafka:2.6.0-debian-10-r106 --namespace default --command -- sleep infinity
15. Run kubectl exec --tty -i kafka-release-client --namespace default -- bash
16. When already exec inside the pod
17. Run kafka-console-producer.sh --broker-list kafka-release-0.kafka-release-headless.default.svc.cluster.local:9092 --topic udacitylogs
18. also run kafka-console-consumer.sh --bootstrap-server kafka-release.default.svc.cluster.local:9092 --topic udacitylogs
        --from-beginning
19. try visit localhost:30000
20. the kafka will show the logs