# ---- Build Stage ----
FROM maven:3.9.7-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn -B --no-transfer-progress package

# ---- Run Stage ----
FROM eclipse-temurin:21-jdk-slim
WORKDIR /app
COPY --from=build /app/target/blog-server-1.0.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]