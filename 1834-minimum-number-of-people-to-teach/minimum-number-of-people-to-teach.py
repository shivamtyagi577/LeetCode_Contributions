class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        m = len(languages)

        # Convert each user's language list to a set for faster lookup
        user_languages = [set(langs) for langs in languages]

        # Identify friendships where users cannot communicate
        non_communicators = []
        for u,v in friendships:
            u_langs = user_languages[u-1]
            v_langs = user_languages[v-1]
            if u_langs.isdisjoint(v_langs):
                non_communicators.append((u,v))
        
        # If all friends can already communicate, no need to teach anyone
        if not non_communicators:
            return 0

        
        # Count how many users need to learn each language to fix all non-communicating pairs
        language_teach_count = defaultdict(set)
        for u, v in non_communicators:
            for lang in range(1, n + 1):
                if lang not in user_languages[u - 1]:
                    language_teach_count[lang].add(u)
                if lang not in user_languages[v - 1]:
                    language_teach_count[lang].add(v)
        
        # Find the minimum number of users to teach for any single language
        min_users_to_teach = min(len(users) for users in language_teach_count.values())

        return min_users_to_teach
