![GitHub Repo stars](https://img.shields.io/github/stars/grei-ufc/DER-cosimul)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/grei-ufc/DER-cosimul)


# This repository is archived, 

The new repository for this project is [tsre-der-opentes](https://github.com/grei-ufc/tsre-der-opentes)

This project is devloped under [GREI](https://grei-ufc.github.io/) Lab. (Smart Grids Research Group) in Federal Universiy of Ceara, Brazil, under supervision of [professor Lucas Silveira](https://lucassm.pro).

This repository contains the Python codes of the DERCosimul project. This project aims to test and validate new control strategies for *Distributed Energy Resources* connected to the electrical distribution grid using **co-simulation** to implent the tests and analisys.

The main analysis consists in implement models for photo-voltaic (PV) sources and battery storage energy systems (BESS) and integrate these models in the power electric grid dynamics, via a powerflow analysis considering a distribution grid system.

The framework used to implement the co-simulation tests is the Python based [Mosaik](https://mosaik.readthedocs.io/en/latest/overview.html) co-simulator system.

Some of the strategies to be implemented in this project are:

- Volt-Watt control;
- Volt-Var control;
- TES control;
- DSM control;
- Control considering batteries storage energy systems (BESS);
- Centralized control.

## How to run this project?

The most easy way to run this project is running it inside a Docker container. There is a Dockerfile in the root directory of this respository to create a container with configured enviroment. How to create and execute this Doccker container is docummented in the [grei-ufc/docker-images](https://github.com/grei-ufc/docker-images/tree/master/DER-cosimul) repository.

## Members

The team members of this project and the holes of each one are described below:

- Victor Gonzaga: grid modeling developement and co-simulation integration;
- João Victor: H2v model development and co-simulation integration;
- Guilherme Mariano: Web tools development for co-simulation data visualization;

## Funding

This project is funded using the Federal University of Ceara Scientific Initiation Program funding. We are very grateful to the university for this initiative.
