```mermaid
erDiagram


Task {
  UUID id
  VARCHAR title
  TEXT description
  VARCHAR attachments
  TEACHER teacher
  DATE dueDate
}

Teacher {
  UUID id
  VARCHAR name
  VARCHAR imageUrl
  VARCHAR email
  VARCHAR about
}

Class {
  UUID id
  VARCHAR name
  VARCHAR schedule
  VARCHAR weekDay
  TEACHER teacher
}

Resource {
  UUID id
  VARCHAR name
  VARCHAR url
  CLASS class
}

Notice {
  UUID id
  VARCHAR title
  TEXT text
}

Resource }|--|| Class : has_many
Task ||--|| Teacher : has
Class ||--|| Teacher : has
```
