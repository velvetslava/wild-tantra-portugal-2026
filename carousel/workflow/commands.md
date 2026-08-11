# Команды проекта

Все команды выполняются из каталога `carousel/`.

## Экспорт 12 PNG и ZIP

```bash
python3 workflow/skills/instagram-carousel-ai-first/scripts/export_slides.py \
  --html index.html \
  --out-dir png \
  --zip download/wild-tantra-carousel-12-slides.zip
```

## Сборка обзорного листа

```bash
python3 workflow/scripts/make_contact_sheet.py \
  --input-dir png \
  --output contact-sheet.jpg \
  --columns 3
```

## Быстрая проверка количества и размеров

```bash
find png -maxdepth 1 -name 'slide-*.png' | sort
sips -g pixelWidth -g pixelHeight png/slide-*.png
```

Ожидаемый результат: 12 файлов, каждый 1080 × 1350 px.
