FROM openjdk:18-jdk-slim-bullseye

WORKDIR /app

COPY App.java .
COPY Helper.java .

# produit en sortie un fichier "App" en bytecode (destiné à la machine virtuelle java)
RUN javac App.java

CMD ["java", "App"]