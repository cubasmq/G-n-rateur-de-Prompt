
import streamlit as st

st.set_page_config(page_title="Générateur de Prompt Expert", layout="centered")

st.title("🧠 Générateur de Prompt Engineering Expert")

st.markdown("""
Ce formulaire t'aide à générer un **prompt expert structuré** pour ChatGPT ou tout autre LLM.
Complète les champs ci-dessous et génère un prompt prêt à copier.
""")

# Initialisation de session
if "generated_prompt" not in st.session_state:
    st.session_state.generated_prompt = ""

# Form fields
role = st.text_input("Quel est le rôle que doit jouer l'IA ? (ex : juriste, marketeur, développeur IA)")
public = st.text_input("Pour qui travaille-t-elle ? (ex : TPE média, jeunes 15-25 ans, entreprise en difficulté)")
mission = st.text_area("Quelle est sa mission précise ? (ex : créer une campagne, analyser un contrat...)")
contraintes = st.text_area("Contraintes à respecter (ton, style, durée, format, droit applicable...)")
format_reponse = st.text_input("Format attendu (ex : tableau, PDF, script Python, etc.)")
question_first = st.checkbox("Demander à l’IA de poser des questions si besoin avant de répondre ?", value=True)

# Bouton Générer
if st.button("🎯 Générer le Prompt"):
    prompt = f"""
Agis en tant que {role} pour {public}.
Ta mission est de {mission}.
Contraintes : {contraintes}.
Donne-moi la réponse sous forme de : {format_reponse}.
"""
    if question_first:
        prompt += " Pose-moi des questions si certains éléments sont flous avant de générer la réponse."

    st.session_state.generated_prompt = prompt.strip()

# Affichage et actions
if st.session_state.generated_prompt:
    st.subheader("📝 Prompt Généré :")
    st.text_area("📋 Copie ton prompt ici", value=st.session_state.generated_prompt, height=200, key="display_prompt")

    st.download_button(
        label="⬇️ Télécharger le prompt (.txt)",
        data=st.session_state.generated_prompt,
        file_name="prompt_expert.txt",
        mime="text/plain"
    )

    if st.button("🧹 Effacer le Prompt"):
        st.session_state.generated_prompt = ""
        st.experimental_rerun()
