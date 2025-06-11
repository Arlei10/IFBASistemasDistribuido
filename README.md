# IFBASistemasDistribuido

1. Clone ou Baixe os Arquivos

Primeiro, certifique-se de que os três arquivos (servidor.py, cliente_saj.py, cliente_laje.py) estão na mesma pasta.

2. Inicie o Servidor

Abra um terminal, navegue até a pasta do projeto e execute o seguinte comando:

Bash

python servidor.py
O servidor irá iniciar e exibirá a mensagem: [ESCUTANDO] Servidor está escutando.... Deixe este terminal aberto.

3. Inicie o Primeiro Cliente (Sensor SAJ)

Abra um segundo terminal, navegue até a mesma pasta e execute:

Bash

python cliente_saj.py
Você verá as mensagens de conexão e envio de dados deste cliente. No terminal do servidor, você verá o log correspondente à chegada desses dados.

4. Inicie o Segundo Cliente (Sensor Laje)

Abra um terceiro terminal, navegue até a pasta e execute:

Bash

python cliente_laje.py
Agora, o segundo cliente também começará a enviar dados.

5. Observe os Resultados

Observe o terminal do servidor. Você verá os logs de dados dos sensores "SAJ" e "Laje" chegando de forma intercalada, demonstrando que o servidor está lidando com ambos simultaneamente.
