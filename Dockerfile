FROM alpine:3.18
RUN apk add --no-cache curl
CMD ["echo", "Welcome to our GitOps Deployable App Container Engine!"]