# Render iteration-plan.qmd to docx
# Run this script from RStudio or via:
#   Rscript status-reports/render_iteration_plan.R

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

rmarkdown::render(
  "iteration-plan.qmd",
  output_format = rmarkdown::word_document(
    reference_docx = "_templates/report-template.docx"
  ),
  output_file = "iteration-plan.docx"
)


