{{- define "todo-app.name" -}}
todo-app
{{- end }}

{{- define "todo-app.fullname" -}}
{{ .Release.Name }}-{{ include "todo-app.name" . }}
{{- end }}

{{- define "todo-app.labels" -}}
app.kubernetes.io/name: {{ include "todo-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: Helm
{{- end }}

{{- define "todo-app.selectorLabels" -}}
app.kubernetes.io/name: {{ include "todo-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "todo-app.serviceAccountName" -}}
{{ .Values.serviceAccount.name | default "default" }}
{{- end }}
