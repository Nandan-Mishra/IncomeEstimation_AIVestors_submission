## For Model

## Copy the entire directory in your code editor named `ml-pipeline_backup`. Then go to the `README.md` file of this directory and follow the steps to run the model.


## For project

## Full Stack AI Finance Platform with Next JS, Supabase, Tailwind, Prisma, Inngest, ArcJet, Shadcn UI 🔥🔥

![banner](https://github.com/Nandan-Mishra/IncomeEstimation_AIVestors_submission/blob/main/public/Main.jpeg)


This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).



## 1. Breif Overview of project and its keyfeatures

A brief overview of your project and its key features
Full Stack AI Finance Platform is a modern web application built using Next.js, Supabase, Prisma, Tailwind CSS, Inngest, ArcJet, and Shadcn UI.
The platform acts as a personal finance assistant powered by AI, offering budgeting, transaction categorization, insights, and secure identity verification.

🔑 Key Features:
🧠 AI-Powered Budgeting: Analyze and categorize user expenses using LLMs.

📊 Smart Insights: Auto-generated recommendations based on financial behavior.

🔐 Clerk Auth Integration: Secure login and onboarding flow.

💬 GEMINI API: Used for personalized financial conversation and suggestions.

📨 Email Alerts via RESEND: Notify users for overspending or budget goals.

⚙️ Inngest for Workflow Automation: Background jobs for data processing and alerts.


## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.js`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!
Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

## Make sure to create a .env file with following variables -
```bash
DATABASE_URL=
DIRECT_URL=

NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/onboarding
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/onboarding

GEMINI_API_KEY=

RESEND_API_KEY=

ARCJET_KEY=
```
