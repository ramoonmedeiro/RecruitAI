from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain


class RecruitAI:

    def __init__(self, open_ai_key: str) -> None:

        self.open_ai_key = open_ai_key
        self.memory = ConversationBufferWindowMemory(k=5)
        self.llm = ChatOpenAI(
            openai_api_key=self.open_ai_key,
            model="gpt-3.5-turbo",
            temperature=0.0
        )
        self.conversation_llm = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=False
        )

    def chat(self, text: str):
        return self.conversation_llm.predict(input=text)

    @classmethod
    def get_prompt_for_analysis(
        requirements: str,
        curriculum: str
    ) -> str:

        prompt = f"""
Você é o melhor recrutador de todos os tempos. Você está analisando um currículo de um candidato para uma vaga de emprego.
Esta vaga poderá ser de diversas áreas e para diversos cargos.
Você deve exclusivamente se basear nos requisitos passados abaixo. Os requisitos poderão ser a própria descrição da vaga
ou algumas exigências que o candidato deve ter para ocupar a vaga ou ambos.
Primeiro, você deve criar uma etapa fazendo um resumo das qualidades do candidato e destacar pontos que são de extremo
interesse da vaga. Após a etapa anterior, você deve dar pontuações para cada caracterísitica que você observar no currículo do
candidato e dar uma pontuação de 0 a 10, sendo 0 para o candidato que não atende a característica e 10 para o candidato que atende perfeitamente 
a característica. Pode ser que o currículo tenha caracterísiticas a mais do que é pedido, se esses requisitos forem interessantes
para a vaga, vale a pena destacar esses pontos.
Ao final, você deverá dar uma nota final geral (também entre 0 a 10) deste candidato se baseando nas pontuações anteriores.

O resultado deve ser da forma:

Nome do Candidato: Resumo do candidato.

Requisitos:
As notas para cada requisito irão vir aqui.

Resultado Final:
Nota geral final irá vir aqui.

Requisitos:
{requirements}

Currículo do Candidato:
{curriculum}

    """
        return prompt
