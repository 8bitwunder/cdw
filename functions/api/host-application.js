const ZOHO_WEB_TO_LEAD_URL = 'https://crm.zoho.com.au/crm/WebToLeadForm';
const SUCCESS_URL = 'https://canberradataweek.com/host_apply_complete';
const CDW_FORM_TOKEN = 'cdw-host-form-v1';
const MINIMUM_COMPLETION_TIME_MS = 4000;
const SPAM_PATTERNS = /\[url=|\[link=|telegram|bitcoin|crypto|casino|viagra/i;

function isRejectedSubmission(formData, now = Date.now()) {
  const token = formData.get('cdw_form_token');
  const loadedAt = Number(formData.get('cdw_form_loaded_at'));
  const honeypot = String(formData.get('cdw_website') || '').trim();
  const zohoHoneypot = String(formData.get('aG9uZXlwb3Q') || '').trim();
  const description = String(formData.get('Description') || '').trim();
  const contributionDetails = description
    .split('\n')
    .find((line) => line.startsWith('CDW Contribution Details: '));
  const idea = contributionDetails
    ? contributionDetails.slice('CDW Contribution Details: '.length).trim()
    : '';

  return token !== CDW_FORM_TOKEN ||
    !Number.isFinite(loadedAt) ||
    now - loadedAt < MINIMUM_COMPLETION_TIME_MS ||
    honeypot.length > 0 ||
    zohoHoneypot.length > 0 ||
    idea.length < 20 ||
    SPAM_PATTERNS.test(idea);
}

export async function onRequestPost({ request }) {
  const formData = await request.formData();

  if (isRejectedSubmission(formData)) {
    return new Response(null, { status: 204 });
  }

  formData.delete('cdw_form_token');
  formData.delete('cdw_form_loaded_at');
  formData.delete('cdw_website');

  const zohoResponse = await fetch(ZOHO_WEB_TO_LEAD_URL, {
    method: 'POST',
    body: formData,
    redirect: 'manual'
  });

  if (!zohoResponse.ok && (zohoResponse.status < 300 || zohoResponse.status >= 400)) {
    return new Response('Unable to submit the form. Please try again.', { status: 502 });
  }

  return Response.redirect(SUCCESS_URL, 303);
}

export { isRejectedSubmission };
