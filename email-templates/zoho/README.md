# Zoho CRM email templates

This folder is the working source for Canberra Data Week transactional email templates. Edit and review templates here before copying them into Zoho CRM.

## Current templates

| Purpose | Zoho module | Suggested template name | Subject | HTML source |
| --- | --- | --- | --- | --- |
| Mailing-list submission | Contacts | `CDW - Mailing List - Submission Acknowledgement` | `You're on the Canberra Data Week mailing list` | `mailing-list-acknowledgement.html` |
| Host application | Leads | `CDW - Host Application - Submission Acknowledgement` | `We've received your Canberra Data Week host application` | `host-application-acknowledgement.html` |

Matching `.txt` files provide plain-text copy for review or for Zoho's plain-text mode.

## Create a template in Zoho CRM

Zoho menu labels can vary slightly by CRM edition, but the workflow is:

1. Open **Setup**, then **Customization > Templates > Email**.
2. Select **New Template** and choose the correct module: **Contacts** for the mailing-list form or **Leads** for the host form.
3. Enter the suggested template name and subject from the table above.
4. In the **Template Gallery**, choose **Insert HTML code / Plain text**. Do not choose a Blank template and then edit its rich-text source.
5. Select the **HTML** icon in the insertion screen.
6. Open the matching `.html` file in this folder and copy the entire fragment. The files intentionally begin with `<style>` and a `<div>` rather than a second `<html>`, `<head>`, or `<body>` document.
7. Paste the fragment into the HTML insertion dialog and select **Insert**.
8. Enter the template name and subject, then use **Preview** to inspect desktop and narrow layouts.
9. Save the template. Configure **From** and **Reply To** in the workflow or sending screen where Zoho requests them; current Zoho versions do not store those fields on the template page.
10. Send a test to an internal address and inspect it in both desktop and mobile mail clients before enabling automation.

Do not paste these files into the normal visual editor or its `</>` rich-text source view. That editor wraps and sanitizes pasted documents and can remove tables, headings, links, and inline styles. Use the dedicated **Insert HTML code / Plain text** option from the Template Gallery.

### Recover from stripped HTML

If Zoho shows the wording but the design, buttons, and tables have disappeared:

1. Discard that template version or create a new test template.
2. Return to the Template Gallery and choose **Insert HTML code / Plain text**.
3. Paste the matching fragment through the **HTML** icon and select **Insert**.
4. Preview before making any visual-editor changes.
5. After saving, reopen the HTML view and verify that `<table`, `<a`, and their `style` attributes are still present.

Do not continue editing a sanitized version: adding the missing text back will not restore the removed structure.

## Connect the templates to the forms

Templates do not send by themselves. Create or update Zoho workflow rules so each new web-form record receives the matching acknowledgment:

- **Contacts workflow:** trigger when a Contact is created by the Canberra Data Week mailing-list Web-to-Contact form, then send the mailing-list template to the Contact email field.
- **Leads workflow:** trigger when a Lead is created by the Canberra Data Week host Web-to-Lead form, then send the host-application template to the Lead email field.

Use criteria that uniquely identify these web forms if other integrations also create Contacts or Leads. Confirm the exact source field/value on test records before enabling the workflow for production.

## Merge fields

The current acknowledgments deliberately avoid merge fields, so they can be pasted without unresolved tokens and the mailing-list template does not need to address someone by last name.

For future personalization:

1. Place the cursor in Zoho's visual editor where the value should appear.
2. Type `#` and select a field from Zoho's merge-field list.
3. Use only fields available on the template's module.
4. Provide wording that still reads naturally when optional data is blank.
5. Never type or guess Zoho merge-tag syntax directly in these source files. Insert it through Zoho and record the verified tag here afterward if the source is brought back into the repository.

## Authoring rules for future templates

- Start from one of the existing HTML files to retain the CDW visual system.
- Use a table-based layout with a maximum width of 600px.
- Keep critical styles inline for email-client compatibility. VS Code warnings about inline CSS are expected for these files.
- Keep the mobile media query at the start of the fragment. Zoho supplies the outer HTML document and viewport meta tag.
- Use absolute `https://` links, never relative links.
- Use hosted, publicly accessible HTTPS URLs for any future images. Do not embed local file paths.
- Include useful preheader text in the hidden first `<div>`.
- Keep acknowledgments factual. Receipt of a host submission must not imply approval.
- Avoid promised response times unless an operational service level has been agreed.
- Keep the HTML under Zoho's 200,000-character limit and attachments below 3 MB.
- Update both HTML and plain-text versions when wording changes.

## Test checklist

1. Preview the template in Zoho at desktop and mobile widths.
2. Verify all links and the Reply To address.
3. Submit each live web form with a test address.
4. Confirm the correct Contact or Lead is created with the expected source data.
5. Confirm only the matching acknowledgment is sent and it arrives once.
6. Check subject, preheader, spacing, button, footer, and plain-text rendering.
7. Check Gmail, Outlook desktop, Outlook web, and one mobile client when available.
8. Confirm the website return page and Zoho workflow both complete successfully.

## Change workflow

Treat these files as the source of truth. After changing a template in Zoho, bring the final HTML back into this folder so the CRM version and repository do not drift. Record material wording or workflow changes in the commit or pull-request description.
