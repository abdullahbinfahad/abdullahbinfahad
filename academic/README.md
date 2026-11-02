# রৈখিক বীজগণিত সহজে

সহজ বাংলায় রৈখিক বীজগণিতের ভিত্তি শেখার একটি রঙিন, মোবাইল-উপযোগী reference page। প্রতিটি বিষয় ছোট নিয়ম, শর্ত, সূত্র, হাতে-কলমে উদাহরণ এবং নিজস্ব SVG চিত্র দিয়ে বোঝানো হয়েছে।

## বিষয়বস্তু

রৈখিক সমীকরণ ও row reduction; matrix algebra এবং `AX=B`; determinant, inverse ও cofactor; vector, dot product ও projection; vector space, subspace, span, independence, basis ও dimension; চারটি fundamental subspace ও rank–nullity; linear transformation ও change of basis; eigenvalue, eigenvector ও diagonalization; orthogonality এবং least squares। এটি মৌলিক ও মধ্যবর্তী ধারণার শেখার সহায়িকা—উন্নত গবেষণার প্রতিটি শাখার পূর্ণ পাঠ্যবই নয়।

## স্থানীয়ভাবে চালানো

```bash
pnpm install --frozen-lockfile
pnpm dev:static
```

তারপর `http://localhost:3000` খুলুন। TypeScript যাচাই ও static build:

```bash
pnpm check
pnpm build:static
```

## GitHub Pages সাবপাথ

`pnpm build:pages` nested path `./` দিয়ে static bundle তৈরি করে এবং generated files এই `academic/` folder-এর root-এ কপি করে। GitHub Pages এই folder-টিকে repository-র existing site domain-এর `/academic/` subpath-এ পরিবেশন করে।

```bash
pnpm build:pages
```

## গুরুত্বপূর্ণ সীমা

সূত্র ব্যবহার করার আগে শর্ত পড়ুন—বিশেষ করে inverse, determinant, projection এবং least-squares-এর ক্ষেত্রে। Calculator বা software-এর output মূল সমীকরণে বসিয়ে যাচাই করুন।
