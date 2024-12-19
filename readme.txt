Aida Argente Sanchis, 20495676P

 ------------
| Práctica 9 |
 ------------

1. Creación ALIAS:
    - Comando usado: git config --global alias.st status 
    - Se han creado los siguientes alias:
        - st: para 'git status'
        - co: para 'git checkout'
        - br: para 'git branch'
        - cm: para 'git commit'

2. Creación RAMAS:
    - Comando usado para crear las ramas en local: git branch nombreRama
    - Comando usado para subir las ramas al repositorio remoto: git push origin nombreRama
    - Se han creado las siguientes ramas:
        - mejora-taxi
        - arreglo-input
        - optimizacion-generacion

3. Proceso 'git bisect':
    1. Se comienza el proceso de buscar el fallo:
        · git bisect start
    2. Se pone como 'bad' el commit actual porque se sabe que este ya contiene el fallo:
        · Comando: git bisect bad
        · Respuesta de la terminal: status: waiting for good commit(s), bad commit known
    3. Para saber todos los commits que he hecho y encontrar el bueno:
        · Comando: git log             
            commit aa0c6386735a1826e65dba023e58d3a37f10aaef (HEAD -> main)
            Author: Aida Argente <aas141@alu.ua.es>
            Date:   Thu Dec 19 18:26:29 2024 +0100

                Mejorada la validación de la entrada para el número de taxis

            commit 0b078e5915ced87d8e01411c85c4141fc97f97a5
            Author: Aida Argente <aas141@alu.ua.es>
            Date:   Thu Dec 19 18:25:19 2024 +0100

                Añadida función para marcar taxi como ocupado

            commit f14e08ffab79fd42706addc6dc1c70f3813088ba
            Author: Aida Argente <aas141@alu.ua.es>
            Date:   Thu Dec 19 18:25:01 2024 +0100

                Añadida función para autenticar a los taxis

            commit 2713a3e14dae83068ee0bf55cde88af895446c58
            Author: Aida Argente <aas141@alu.ua.es>
            Date:   Thu Dec 19 18:24:42 2024 +0100

                Añadida función para cambiar la posición del taxi

            commit 37cc13320b2bc03860981c2ec9ecee0d37cac3da
            Author: Aida Argente <aas141@alu.ua.es>
            Date:   Thu Dec 19 18:24:04 2024 +0100

                Cambio del estado por defecto de los taxis a 'EN RUTA'

            commit 2cdcbd54f4e8bb0e0ad20ccbff0c79fa55c30192
            Author: Aida Argente <aas141@alu.ua.es>
            Date:   Thu Dec 19 18:22:13 2024 +0100

                Introducir fallo en generador.py

            commit 69239f73508ddd568acf16cb7f560e10e4d7bc68 (origin/optimizacion-generacion, origin/mejora-taxi, origin/main, origin/arreglo-inp
            ut, optimizacion-generacion, mejora-taxi, arreglo-input)
            Author: Aida Argente <aas141@alu.ua.es>
            Date:   Thu Dec 19 17:55:35 2024 +0100

                Subir código Python
    4.  Cuando encuentras el commit bueno se pone su identificador para localizarlo:
        · Comando: git bisect good 69239f73508ddd568acf16cb7f560e10e4d7bc68
        · Respuesta de la terminal: Bisecting: 2 revisions left to test after this (roughly 2 steps)
                                    [2713a3e14dae83068ee0bf55cde88af895446c58] Añadida función para cambiar la posición del taxi
    5. Como dice que hay que revisar 2 commits más para verificar el inicio del fallo, te señala cuál es el siguiente commit al que tienes que ir
       te diriges a ese para marcarlo como bueno o malo:
        · Comando: git checkout 2713a3e14dae83068ee0bf55cde88af895446c58
        . Respuesta de la terminal: HEAD is now at 2713a3e Añadida función para cambiar la posición del taxi
    6. Marcar commit como malo porque observas en el código que contiene el fallo:
        · Comando: git bisect bad
        · Respuesta de la terminal: Bisecting: 0 revisions left to test after this (roughly 1 step)
                                    [37cc13320b2bc03860981c2ec9ecee0d37cac3da] Cambio del estado por defecto de los taxis a 'EN RUTA'
    7. Repetir el paso 5 y 6 ya que al cambiar al commit indicado se sigue observando el fallo.
        . Al marcar el commit como malo la respuesta del proceso es la siguiente:                                 
            Bisecting: 0 revisions left to test after this (roughly 0 steps)
            [2cdcbd54f4e8bb0e0ad20ccbff0c79fa55c30192] Introducir fallo en generador.py
        · Al observar que no queda ningún paso, ya sabes que el commit que te está señalando es el que ha originado el fallo.
    8. Terminas el proceso de 'git bisect'
        · Comando: git bisect reset
        · Respuesta terminal: Previous HEAD position was 2cdcbd5 Introducir fallo en generador.py
                              Switched to branch 'main'
    8. Arreglas el fallo y lo subes a github.

4. Hook para evitar commits con mensajes vacíos:
    1. Abrir el archivo .git/hooks/commit-msg:
        ·Comando: nano .git/hooks/commit-msg
    2. Se añade este contenido:
        #!/bin/sh
        if [ -z "$1" ]; then
            echo "El mensaje del commit no puede estar vacío."
            exit 1
        fi
    3. Se le dan permisos al hook:
        · Comando: chmod +x .git/hooks/commit-msg
    4. Si pruebo a añadir un commit vacío me sale el siguiente error:
        · Subir a git el 'readme.txt': git add readme.txt
        · Commit vacío: git commit -m ""
            · Respuesta de la terminal: Aborting commit due to empty commit message.
        · Commit no vacío: git commit -m "Mensaje de commit válido"
            · Respuesta de la terminal: [main 49772b9] Mensaje de commit válido
                                        1 file changed, 106 insertions(+)
                                        create mode 100644 readme.txt
