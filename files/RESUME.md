# Resume / CV

The `/cv/` page and `Taoyu_Lyu_CV.pdf` in this folder are generated automatically.
Do not edit them here.

Source of truth: `resume.tex` in the private repo `ChrisLvvvv/CV_Git`, which is
linked to the Overleaf CV project.

To update:

1. Edit the CV in Overleaf.
2. Overleaf → Menu → GitHub → **Push Overleaf changes to GitHub**.
3. The "Sync CV from Overleaf" workflow (`.github/workflows/sync-cv.yml`) runs
   hourly, or run it right away from the Actions tab → Sync CV from Overleaf →
   Run workflow. It compiles the PDF, regenerates `_data/cv_tex.json`, commits
   both, and starts a Pages rebuild.

The parser is `scripts/cv_from_tex.py`. It expects the current template:
`\subsection*{\Large Section}`, entries as `\item \headerrow{..}{..} \headerrow{..}{..}`
followed by `itemize*` bullets, and skills as `\item \textbf{Label:} text`.
The phone number is never exported to the web page.
