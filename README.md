# TechTest

Section intented to explain the execution of the differnet exercises.

To begin, first step is to clone the repository.

## 1.1

```bash
  cd 1.1
  ansible-playbook site.yml
```

## 1.2

```bash
  export OWM_API_KEY="xxxx"
  export OWM_CITY="<desired_city>"
  cd 1.2 - 1.3
  python3 getweather.py
```

## 1.3

```bash
  cd 1.2 - 1.3
  docker build . --tag=getweather:dev
  docker run --rm -e OWM_API_KEY="xxxx" -e OWM_CITY="<desired_city>" getweather:dev

  ------ or ------

  docker pull venegator/getweather:dev
  docker run --rm -e OWM_API_KEY="xxxx" -e OWM_CITY="<desired_city>" venegator/getweather:dev
```

## 2.1

```bash
sudo apt install nmap ndiff
cd 2
./scanner.sh <ip/iprange/domain> (format 0-255.0-255.0-255.0-255)
```

## 2.2

Using minikube.

```bash
cd 2/kubernetes/
kubectl create -f scanner-pvc.yaml
kubectl create -f scanner-cj.yaml
```
