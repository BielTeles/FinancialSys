 - Projeto realizado como teste para a empresa MaxiProd
 - A ideia é a seguinte:


Objetivo:

       Implementar um sistema de controle de gastos residenciais com:
       
       Cadastros de transações;
       
       Cadastro de pessoas;
       
       Consulta de totais;
       
       Deixar claro qual foi a lógica/função do que foi desenvolvido, através de comentários e documentação no próprio código. 



Especificação:
       Em linhas gerais, basta que o sistema cumpra os requisitos apresentados, não sendo necessária preocupação com os casos inesperados, apresentação (visual), etc.



Tecnologias:
       Quaisquer*, bastando que o sistema final ofereça as funcionalidades descritas a seguir. Ainda, não é obrigatório utilizar banco de dados, podendo-se manter os dados em memória da maneira que bem entender.
       
       Caso não tenha preferência por alguma stack tecnológica, sugerimos utilizar a nossa atual: .NET com C# para o back-end e React com Typescript para o front-end.
       
       * Preferencialmente alguma tecnologia web, se possível utilizando arquitetura MVC. Caso não tenha experiência com nenhuma, uma aplicação de linha de comando basta.


Funcionalidades:
      Cadastro de pessoas: 
      
      Deverá ser implementado um cadastro contendo as funcionalidades básicas de gerenciamento: criação, deleção e listagem.
      
      Em casos que se delete uma pessoa, todas a transações dessa pessoa deverão ser apagadas.
      
      O cadastro de pessoa deverá conter:
      
      Identificador (deve ser um número inteiro sequencial único gerado automaticamente);
      
      Nome (texto);
      
      Idade (número inteiro);



      Cadastro de transações: 
      
      Deverá ser implementado um cadastro contendo as funcionalidades básicas de gerenciamento: criação e listagem (não é necessário implementar edição/deleção).
      
      Caso o usuário informe um menor de idade (menor de 18), apenas despesas deverão ser aceitas.
      
      O cadastro de transação deverá conter:
      
      Identificador (deve ser um número inteiro sequencial único gerado automaticamente);
      
      Descrição (texto);
      
      Valor (número decimal positivo);
      
      Tipo (despesa/receita);
      
      Pessoa (inteiro identificador da pessoa do cadastro anterior);
      
      Esse valor precisa existir no cadastro de pessoa;



Consulta de totais:

     Deverá listar todas as pessoas cadastradas, exibindo o total de receitas, despesas e o saldo (receita – despesa) de cada uma.
     
     Ao final da listagem anterior, deverá exibir o total geral de todas as pessoas incluindo o total de receitas, total de despesas e o saldo líquido.
