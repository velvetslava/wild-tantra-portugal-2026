# Воспроизводимый workflow карусели

Эта папка позволяет продолжить работу без контекста исходной переписки.

## Быстрый старт

Откройте терминал в каталоге `carousel/` и установите зависимости один раз:

```bash
python3 -m pip install -r workflow/requirements.txt
python3 -m playwright install chromium
```

После правок выполните команды из `workflow/commands.md`.

## Использование с Codex

Скиллы можно оставить в репозитории и попросить Codex прочитать их перед работой. Для установки в личную библиотеку Codex скопируйте каталоги:

```bash
mkdir -p ~/.codex/skills
cp -R workflow/skills/ideal-carousel ~/.codex/skills/
cp -R workflow/skills/instagram-carousel-ai-first ~/.codex/skills/
```

После установки достаточно формулировки: «Продолжи Wild Tantra-карусель, используя `ideal-carousel` и `instagram-carousel-ai-first`; соблюдай `carousel/AGENTS.md`».

## Состав

- `skills/ideal-carousel/` — структура сильной карусели и QA контента;
- `skills/instagram-carousel-ai-first/` — экспортёр, шаблоны и правила версионирования;
- `scripts/make_contact_sheet.py` — сборка общего обзорного листа;
- `commands.md` — готовые команды для текущего проекта;
- `manifest.yaml` — карта канонических входов и выходов;
- `status.yaml` — история состояния и последних решений;
- `history/` — ранние варианты, прототипы, исходники и визуальные ревью.

## Каноническое правило

`../index.html` — единственный финальный HTML. Исторические файлы не редактируются и не публикуются вместо него без явного решения владельца проекта.
