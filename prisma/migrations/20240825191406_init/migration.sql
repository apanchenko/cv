-- CreateTable
CREATE TABLE "Author" (
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "created" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Author_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Address" (
    "id" SERIAL NOT NULL,
    "author_id" INTEGER NOT NULL,
    "icon" VARCHAR(255) NOT NULL,
    "href" VARCHAR(255) NOT NULL,
    "text" VARCHAR(255) NOT NULL,

    CONSTRAINT "Address_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Address" ADD CONSTRAINT "Address_author_id_fkey" FOREIGN KEY ("author_id") REFERENCES "Author"("id") ON DELETE CASCADE ON UPDATE CASCADE;


WITH rows AS (
    INSERT INTO "Author"("name") VALUES ('Anton Panchenko') RETURNING "id"
)
INSERT INTO "Address"("author_id", "icon", "href", "text")
VALUES
    ((SELECT "id" FROM rows), 'icofont-email', 'mailto:apanchenko@gmail.com', 'apanchenko@gmail.com'),
    ((SELECT "id" FROM rows), 'icofont-telegram', 'https://t.me/pazuza', '@pazuza'),
    ((SELECT "id" FROM rows), 'icofont-linkedin', 'https://www.linkedin.com/in/apanchenko', 'linkedin.com/in/apanchenko');
