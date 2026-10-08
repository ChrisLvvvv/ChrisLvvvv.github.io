# Resume PDF

The Resume page stays at `/cv/`. Its PDF source is `/files/Taoyu_Lyu_Resume.pdf`.

Update the document without changing website templates:

1. Edit the resume in Overleaf and compile it.
2. Download the compiled PDF.
3. Save it in this directory as `Taoyu_Lyu_Resume.pdf`, replacing the previous PDF if present.
4. Run `bundle exec jekyll build` to verify the site.
5. Commit and push the PDF when ready to deploy.

Jekyll checks for that exact path during each build. When present, the Resume page displays the native PDF preview and Open Resume / Download PDF actions. When absent, it displays the original factual CV content from `_pages/cv.md` and omits all PDF controls. On mobile, the PDF actions replace the embedded preview.

The website does not compile LaTeX or alter the PDF. Keep the compiled document's original format and page size.
