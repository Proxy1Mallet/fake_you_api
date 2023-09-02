class GetSession:
    def __init__(self, data):
        self.json = data
        self.sucess = None
        self.logged_in = None
        self.user = None
        self.user_token = None
        self.username = None
        self.display_name = None
        self.email_gravatar_hash = None
        self.fakeyou_plan = None
        self.storyteller_stream_plan = None
        self.can_use_tts = None
        self.can_use_w2l = None
        self.can_delete_own_tts_results = None
        self.can_delete_own_w2l_results = None
        self.can_delete_own_account = None
        self.can_upload_tts_models = None
        self.can_upload_w2l_templates = None
        self.can_delete_own_tts_modelsV = None
        self.can_delete_own_w2l_templates = None
        self.can_approve_w2l_templates = None
        self.can_edit_other_users_profiles = None
        self.can_edit_other_users_tts_models = None
        self.can_edit_other_users_w2l_templates = None
        self.can_delete_other_users_tts_models = None
        self.can_delete_other_users_tts_results = None
        self.can_delete_other_users_w2l_templates = None
        self.can_delete_other_users_w2l_results = None
        self.can_ban_users = None
        self.can_delete_users = None

    @property
    def get_sesion(self):
        try:
            self.sucess = self.json['success']
            self.logged_in = self.json['logged_in']
            self.user = self.json['user']
            self.user_token = self.json['user']['user_token']
            self.usrname = self.json['user']['username']
            self.display_name = self.json['user']['display_name']
            self.email_gravatar_hash = self.json['user']['email_gravatar_hash']
            self.fakeyou_plan = self.json['user']['fakeyou_plan']
            self.storyteller_stream_plan = self.json['user']['storyteller_stream_plan']
            self.can_use_tts = self.json['user']['can_use_tts']
            self.can_use_w2l = self.json['user']['can_use_w2l']
            self.can_delete_own_tts_results = self.json['user']['can_delete_own_tts_results']
            self.can_delete_own_w2l_results = self.json['user']['can_delete_own_w2l_results']
            self.can_delete_own_account = self.json['user']['can_delete_own_account']
            self.can_upload_tts_models = self.json['user']['can_upload_tts_models']
            self.can_upload_w2l_templates = self.json['user']['can_upload_w2l_templates']
            self.can_delete_own_tts_models = self.json['user']['can_delete_own_tts_models']
            self.can_delete_own_w2l_templates = self.json['user']['can_delete_own_w2l_templates']
            self.can_approve_w2l_templates = self.json['user']['can_approve_w2l_templates']
            self.can_edit_other_users_profiles = self.json['user']['can_edit_other_users_profiles']
            self.can_edit_other_users_tts_models = self.json['user']['can_edit_other_users_tts_models']
            self.can_edit_other_users_w2l_templates = self.json['user']['can_edit_other_users_w2l_templates']
            self.can_delete_other_users_tts_models = self.json['user']['can_delete_other_users_tts_models']
            self.can_delete_other_users_tts_results = self.json['user']['can_delete_other_users_tts_results']
            self.can_delete_other_users_w2l_templates = self.json['user']['can_delete_other_users_w2l_templates']
            self.can_delete_other_users_w2l_results = self.json['user']['can_delete_other_users_w2l_results']
            self.can_ban_users = self.json['user']['can_ban_users']
            self.can_ban_users = self['user']['can_ban_users']
        except(KeyError, TypeError): pass
        return self

class GetJob:
    def __init__(self, data):
        self.json = data
        self.success = None
        self.state = None
        self.job_token = None
        self.status = None
        self.attempt_count = None
        self.maybe_result_token = None
        self.maybe_public_bucket_wav_audio_path = None
        self.model_token = None
        self.tts_model_type = None
        self.title = None
        self.raw_inference_text = None
        self.created_at = None
        self.updated_at = None

    @property
    def get_job(self):
        self.success = self.json['success']
        self.state = self.json['state']
        self.job_token = self.json['state']['job_token']
        self.status = self.json['state']['status']
        self.attempt_count = self.json['state']['attempt_count']
        self.maybe_result_token = self.json['state']['maybe_result_token']
        self.maybe_public_bucket_wav_audio_path = self.json['state']['maybe_public_bucket_wav_audio_path']
        self.model_token = self.json['state']['model_token']
        self.tts_model_type = self.json['state']['tts_model_type']
        self.title = self.json['state']['title']
        self.raw_inference_text = self.json['state']['raw_inference_text']
        self.created_at = self.json['state']['created_at']
        self.updated_at = self.json['state']['updated_at']
        return self

class Inference:
    def __init__(self, data):
        self.json = data
        self.success = None
        self.inference_job_token = None
        self.inference_job_token_type = None

    @property
    def inference(self):
        try:
            self.success = self.json['success']
            self.inference_job_token = self.json['inference_job_token']
            self.inference_job_token_type = self.json['inference_job_token']
        except(KeyError, TypeError): pass
        return self
