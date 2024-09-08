<!-- markdownlint-disable MD022 MD031 MD032 -->
# CV

Generate resume in PDF format.

## Plans

1. Freemium Model
    - Free features: basic templates, PDF export, limited number of resumes.
    - Paid features: professional templates, advanced editing options.

2. Partnership Programs
    - Advertisements or partner offers: courses, job opportunities, job search training, etc.
    - Collaboration with employment platforms: offer their services through your website.

3. SEO and Career Advice
    - Publishing articles related to career development, job search, and resume writing to attract organic traffic.

4. Resume Writing Services
    - Professional resume writing or expert revision.
    - Resume analysis based on employer requirements.

5. Social Network Integration
    - Integration with LinkedIn, Xing, and other platforms for automatic synchronization and updating of resume data.

## Generate the CV

```shell
docker compose run --rm seed                # seed the database
docker compose down db                      # stop the database

docker compose up --build -d
docker compose down

# dev:
uv venv --python 3.12.4 --preview           # create environment
. .venv/bin/activate.fish                   # activate the environment
uv sync                                     # install dependencies
docker compose run -p 5441:5432 -d db       # run database
prisma db push                              # push schema to database
uvicorn cv.api:app --reload --port 8000    # run local server
```

## Backlog

- editor
- auth
- ci/cd with [github actions](https://docs.github.com/en/actions)
- [dev container](https://code.visualstudio.com/docs/devcontainers/containers)
- consider [tailwindcss](https://tailwindcss.com/)

## Links

- [best-resume-font-size-and-type-2063125](https://www.thebalancecareers.com/best-resume-font-size-and-type-2063125)
- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)
- [playwright](https://playwright.dev/python/)
- [prisma](https://prisma-client-py.readthedocs.io)
- [htmx](https://htmx.org/)
- [examples](https://github.com/marty331/fasthtmx/)

## Peers

- [novoresume](https://novoresume.com/)
- [zety](https://zety.com/resume-builder)
- [resume.io](https://resume.io/)
- [indeed](https://www.indeed.com/create-resume/)
- [resumegenius](https://resumegenius.com/)
- [flowcv](https://flowcv.com/)
- [livecareer](https://www.livecareer.com/resume/builder)
- [enhancv](https://enhancv.com/resume-builder/)
- [resume.com](https://www.resume.com/)
- [cvmaker](https://www.cvmaker.com/)
- [resumekit](https://resumekit.com/)
- [canva](https://www.canva.com/create/resumes/)
